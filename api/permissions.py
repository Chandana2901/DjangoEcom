from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsProducerOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'Producer' and obj.producer == request.user
    