from django.contrib.auth import get_user_model
from rest_framework import serializers

from .. import models

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "url"]


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organization
        fields = ["name", "user", "url"]


class ShelfSerializer(serializers.HyperlinkedModelSerializer):
    label = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = models.Shelf
        fields = ["organization", "size", "available_size", "url", "label"]


class BoxSerializer(serializers.HyperlinkedModelSerializer):
    label = serializers.CharField(source="__str__", read_only=True)
    siblings = serializers.SerializerMethodField()

    class Meta:
        model = models.Box
        fields = ["shelf", "url", "label", "siblings"]

    def get_siblings(self, instance):
        return instance.shelf.box_set.count() - 1
