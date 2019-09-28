from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from django_api.typing import QuerySetType

from .. import models
from . import serializers

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self) -> QuerySetType[User]:
        return User.objects.all()


class OrganizazionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrganizationSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self) -> QuerySetType[models.Organization]:
        return models.Organization.objects.all()


class ShelfViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShelfSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self) -> QuerySetType[models.Shelf]:
        return models.Shelf.objects.all()


class BoxViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BoxSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self) -> QuerySetType[models.Box]:
        if self.request.user.is_superuser:
            return models.Box.objects.all()
        else:
            return models.Box.objects.filter(shelf__organization__user=self.request.user)
