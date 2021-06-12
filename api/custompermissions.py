from rest_framework import permissions


class OwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # In this case, 'SAFE_METHODS' = 'GET' Method such as get User Info,
        # on the other hand, 'DELETE', 'UPDATE' method in NOT 'SAFE_METHODS' because these are gonna 'modify Data'
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.id == request.user.id
