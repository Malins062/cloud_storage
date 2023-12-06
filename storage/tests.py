import logging

from django.test.client import Client
from django.test import TestCase
from users.models.users import User
from .models.folders import Folder

logger = logging.getLogger()
logger.level = logging.INFO

client = Client()
user = User.objects.create_user(username='testadmin', password='admin')
client.login(username='testadmin', password='admin')


class TestMPTT(TestCase):

    def test_create_folders(self):
        folder_1 = Folder.objects.create(owner=user, name='Видео', )
        folder_1_1 = Folder.objects.create(owner=user, name='Фильмы', parent=folder_1)
        folder_1_2 = Folder.objects.create(owner=user, name='Клипы', parent=folder_1)
        folder_1_3 = Folder.objects.create(owner=user, name='Ролики', parent=folder_1)

        logger.info('Folder_1 descendants')
        logger.info(folder_1.get_descendants())

        assert folder_1.get_descendants()
