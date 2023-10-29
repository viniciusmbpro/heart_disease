from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsOwnerAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
