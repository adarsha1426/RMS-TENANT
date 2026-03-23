from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):

        if (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
            and request.user.role == "admin"
        ):
            return True
        return False


class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):

        if (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
            and request.user.role == "staff"
        ):
            return True
        return False


class IsCustomerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
            and request.user.role == "customer"
        )
