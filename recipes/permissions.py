from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsStaffOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or
                # request.method in SAFE_METHODS or
                # request.user.is_moderator or
                # request.user.is_admin
                request.user.is_staff
                )