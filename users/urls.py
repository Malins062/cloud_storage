from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import auth, profile

router = DefaultRouter()
# router.register(r'search', users.UserListSearchView, 'users-search')

urlpatterns = [
    path('users/reg/', auth.RegistrationView.as_view(), name='reg'),
    path('users/change-passwd/', auth.ChangePasswordView.as_view(), name='change_passwd'),
    path('users/profile/', profile.ListView.as_view(), name='profile'),
]

urlpatterns += path('users/', include(router.urls)),
