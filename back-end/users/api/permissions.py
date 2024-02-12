from rest_framework.permissions import BasePermission


class IsChefUser(BasePermission):
    def has_permission(self, request, view):
        return bool().has_permission(request.user, request.user.is_chef)


class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool().has_permission(request.user, request.user.is_manager)


class IsWaiterUser(BasePermission):
    def has_permission(self, request, view):
        return bool().has_permission(request.user, request.user.is_waiter)
