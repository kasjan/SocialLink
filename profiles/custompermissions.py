"""Custompermissions.py file."""
# 3rd-party
from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):  # noqa: D101
    def has_object_permission(self, request, view, obj):  # noqa: D102
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user
