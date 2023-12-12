from django.contrib.auth import get_user_model
from rest_framework import serializers

from storage.models.files import File

User = get_user_model()


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
