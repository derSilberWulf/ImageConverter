from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Only the owner can view and edit images
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the object owner is the same as the requester
        """
        # Only allow the owner to view and edit the object
        return obj.owner == request.user