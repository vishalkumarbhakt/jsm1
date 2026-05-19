from rest_framework.permissions import BasePermission


class HasRole(BasePermission):
    allowed_roles = ()

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role in self.allowed_roles
        )


class IsAdminRole(HasRole):
    allowed_roles = ("admin",)


class IsTeacherRole(HasRole):
    allowed_roles = ("teacher",)


class IsStudentRole(HasRole):
    allowed_roles = ("student",)


class IsTeacherOrAdmin(HasRole):
    allowed_roles = ("teacher", "admin")
