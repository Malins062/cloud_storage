import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()
URL = 'http://127.0.0.1:8000/admin'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(
        email='user@test.ru',
        username='Ivan',
        phone_number='+79998887766',
        password='@wdA331s')


@pytest.mark.django_db
def test_backends_login(client, user):
    # response = requests.get(URL, auth=(user.username, user.password))
    # logged_client = client.force_login(user)
    response = client.force_authenticate(user=user)
    # client.force_login(user=user)
    # client.login(username='user', password='user')
    # response = client.get(URL, follow=True)
    # user = User.objects.get(username='lauren')
    # client = APIClient()
    # response = client.force_authenticate(user=user)
    # print(response)
    assert response.status_code == 200
