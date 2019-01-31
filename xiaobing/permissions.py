from rest_framework.permissions import BasePermission


class AllowAny(BasePermission):
    # '任何人都能访问，和没设置一样'
    def has_permission(self, request, view):
        return True


class IsAuthenticated(BasePermission):
    # '登录后，才能访问'
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
