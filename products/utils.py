from django.http import HttpResponseForbidden


def checkPermission(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to create a category.")
    if request.user.role != 'Producer' :
        return HttpResponseForbidden("You do not have permission to create a category.")
    return None