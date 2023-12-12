from django.urls import path, include
from rest_framework.routers import DefaultRouter

import storage.views.storage

router = DefaultRouter()
router.register(r'storage', storage.views.storage.FileFolderViewSet, 'storage')

urlpatterns = [
]

urlpatterns += path('storage/', include(router.urls)),
