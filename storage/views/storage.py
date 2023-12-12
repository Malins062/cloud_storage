import pdb

from django.contrib.auth import get_user_model
from django.db.models import Q
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiExample
from rest_framework import generics, status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from config.settings import SPECTACULAR_SETTINGS
from storage.models.folders import Folder
from storage.serializers.api.storage import FileFolderSerializer
# from common.views.mixins import ListViewSet
# from users.permissions import IsNotCorporate
from users.serializers.api import auth as user_s

User = get_user_model()


@extend_schema_view(
    post=extend_schema(
        summary='Работа с хранилищем',
        tags=[SPECTACULAR_SETTINGS['TITLES_TAGS']['STORAGE']],
        description='Создание, удаление файлов и папок в хранилище',
    ),
)
class FileFolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FileFolderSerializer


    def get_queryset(self):
        return Folder.objects.filter(parent=None)
