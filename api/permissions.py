# from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsProducerOrReadOnly(BasePermission):
#     def has_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.is_authenticated and request.user.role == 'Producer' and obj.producer == request.user


import requests
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView  
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class GatewayProxyApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    ACCESS_RULES = {
        'category':{
            'Admin': ['GET', 'POST', 'DELETE'],
            'Consumer' : ['GET'],
            'Producer': ['GET'],
        },
        'products':{
            'Admin': ['GET', 'POST', 'DELETE'],
            'Consumer': ['GET'],
            'Producer': ['GET', 'POST', 'DELETE', 'PUT']
        },
        'users':{
            'Admin': ['POST'],
            'Consumer': ['POST'],
            'Producer': ['POST']
        }
    }
    PORTS = {'products': '8002', 'category': '8003', 'users': '8001'}
    
    def handle_request(self, request, service, path=""):
        method = request.method
        userRole = None
        loginPath = service == 'users' and (path == 'login/' or path == 'logout/')
        port = self.PORTS.get(service)
        allowedMethods = []
        
        if not loginPath:
            userRole = request.user.role
            allowedMethods = self.ACCESS_RULES.get(service,{}).get(userRole,[])
            if method not in allowedMethods:
                return JsonResponse({
                    'error': 'unauthorized'
                }, status=403)
        
        targetUrl = f"http://127.0.0.1:{port}/{service}/{path}"
        
        headers = {
            'X-User-Id': str(request.user.id),
            'X-User-Role': userRole,
            'Authorization': request.headers.get('Authorization', '')
        }
        if request.method == 'POST':
            payload = request.POST.dict()
            payload.pop('csrfmiddlewaretoken', None)
        else:
            payload = None
        try:
            response = requests.request(
                method=method,
                url=targetUrl,
                headers=headers,
                params=request.GET,
                json=payload,
                timeout=5
            )
            data = response.json()
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'error': 'service unavailable',
                'details': str(e)
            }, status=503)
        
        data['_ui_permissions'] = {
            'can_create': 'POST' in allowedMethods,
            'can_delete': 'DELETE' in allowedMethods,
            'can_update': 'PUT' in allowedMethods,
            'role_label': userRole
        }
        
        return JsonResponse(
            data,
            status=response.status_code,
        )
    
    def get(self, request, service, path=""):
        return self.handle_request(request, service, path)
    
    def post(self, request, service, path=""):
        return self.handle_request(request, service, path)
    
    def delete(self, request, service, path=""):
        return self.handle_request(request, service, path)
    
    def put(self, request, service, path=""): 
        return self.handle_request(request, service, path)