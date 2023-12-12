from django.contrib.auth import get_user_model
from rest_framework import serializers

from storage.models.files import File
from storage.models.folders import Folder

User = get_user_model()


class FileFolderSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        if isinstance(obj, Folder):
            serializer = self.__class__(obj.children, many=True)
            return serializer.data
        return None

    class Meta:
        model = Folder
        fields = '__all__'
