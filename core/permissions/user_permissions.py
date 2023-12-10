from rest_framework.permissions import BasePermission, IsAdminUser


# створити свій пермішин по аналогії з джангівським IsAdminUser , і назвемо  його IsSuperUser
# і використаємо його в створенні автопарку - тільки супер юзер може
class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
