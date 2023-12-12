from django.contrib.auth import get_user_model
from rest_framework import serializers

from storage.models.folders import Folder
from storage.serializers.api.files import FileSerializer

User = get_user_model()


class DirectorySerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = '__all__'
