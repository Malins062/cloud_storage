from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/', include('api.urls'), name='api'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]
