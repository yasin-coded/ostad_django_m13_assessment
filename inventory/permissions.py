from rest_framework import permissions

class IsStaffOrAdminOrReadOnly (permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and request.user.role in ['ADMIN', 'STAFF']
        )
        
