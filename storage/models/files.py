import os
from django.contrib.auth import get_user_model
from django.db import models
from django.core.files.storage import FileSystemStorage
from common.models.mixins import BaseInstanceStorageModel
from config.settings import MEDIA_ROOT
from storage.models.folders import Folder

# Path to file storage
fs = FileSystemStorage(location=os.path.join(MEDIA_ROOT, 'fs'))

# User
User = get_user_model()


# Path to user files
def get_upload_path(instance, filename):
    return f'user_{instance.creator.id}/{filename}'


class File(BaseInstanceStorageModel):
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='files', verbose_name='Владелец'
    )
    # description = models.TextField(verbose_name='Описание файла', blank=True)
    # name = models.CharField(max_length=255, unique=True, verbose_name='Наименование файла')
    file = models.FileField(upload_to=get_upload_path, storage=fs, verbose_name='Файл',)
    folder = models.ForeignKey(to=Folder, on_delete=models.CASCADE, verbose_name='Папка', blank=True, null=True)
    # url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-created_at']

    def __str__(self):
        return self.file.name


# class FileScope(models.Model):
#     id = models.AutoField(unique=True, primary_key=True)
#     file = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name='Файл', related_name='scopes')
#     folder = models.ForeignKey(Folder, on_delete=models.CASCADE, verbose_name='Папка', related_name='scopes')
#
#     class Meta:
#         verbose_name = 'Папка файла'
#         verbose_name_plural = 'Папки файлов'
#
#     def __str__(self):
#         return f'#{self.id} - {self.folder}'
