from rest_framework.permissions import BasePermission

# Notes: Il est aussi possible d'utiliser les restrictions: GLOBAL / OBJECT-LEVEL

# pour le contributeur:
    # existe un contrib avec:
        # user_id == request.user.id
        # project_id == project_pk ou pk

# pour l'author:
    # existe un project avec:
        # author_id == request.user.id
        # id == project_pk ou pk

class IsAuthor(BasePermission):

    def has_permission(self, request, view):

        if view.action == 'list':
            return bool(request.user and request.user.is_authenticated)
        elif view.action == 'retrieve':
            return bool(request.user and request.user.is_authenticated)
        elif view.action == 'create':
            return bool(request.user and request.user.is_authenticated)
        elif view.action == 'update':
            return bool(request.user and request.user.is_authenticated)
        elif view.action == 'destroy':
            return bool(request.user and request.user.is_authenticated)


class IsContributor(BasePermission):

    def has_permission(self, request, view):

        if view.action == 'list':
            return bool(request.user and request.user.is_authenticated)
        elif view.action == 'retrieve':
            return bool(request.user and request.user.is_authenticated)
        elif view.action == 'create':
            return bool(request.user and request.user.is_authenticated)
        elif view.action == 'update':
            False
        elif view.action == 'destroy':
            False
