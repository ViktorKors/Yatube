from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Проверяет является ли отправитель запроса автором определенного поста.
    """

    def has_object_permission(self, request, view, obj):
        """Фунцкия для проверки пользователя"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
