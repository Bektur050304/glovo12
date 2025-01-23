from rest_framework import permissions



class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Администратор'


class CheckOwnerEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class CheckAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Клиент'
