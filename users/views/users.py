import pdb

from django.contrib.auth import get_user_model
from django.db.models import Q
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# from common.views.mixins import ListViewSet
# from users.permissions import IsNotCorporate
from users.serializers.api import users as user_s

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
)
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = user_s.RegistrationSerializer
