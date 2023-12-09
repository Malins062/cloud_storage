from rest_framework import serializers
from rest_framework.generics import get_object_or_404


class ExtendedModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
