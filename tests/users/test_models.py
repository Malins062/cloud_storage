import pytest
from rest_framework.exceptions import ParseError
from django.contrib.auth import get_user_model


@pytest.fixture
def user_model():
    return get_user_model()
    
    
@pytest.mark.django_db
def test_create_users(user_model):
    with pytest.raises(ParseError):
        user_model.objects.create_user(password='@wdA331s')

    with pytest.raises(ParseError):
        user_model.objects.create_user(username='admin', password='@wdA331s')

    user = user_model.objects.create_user(email='user@test.ru', first_name='Ivan', last_name='Ivanov', password='@wdA331s')
    assert user.__str__() == f'Ivan Ivanov #{user.pk}'

    user = user_model.objects.create_user(email='user1@User.ru', password='@wdA331s')
    assert user.email == 'user1@user.ru'
    assert user.username == user.email

    user = user_model.objects.create_user(email='user5@test.ru', password='@wdA331s')
    assert not user.is_staff
    assert not user.is_superuser
    assert user.is_active


@pytest.mark.django_db
def test_create_superusers(user_model):
    with pytest.raises(ParseError):
        user_model.objects.create_superuser(password='@wdA331s')

    user = user_model.objects.create_superuser(username='admin', email='admin@admin.ru', password='@wdA331s')
    assert user.is_staff
    assert user.is_superuser
    assert user.is_active
