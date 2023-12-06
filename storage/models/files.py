import os
from django.contrib.auth import get_user_model
from django.db import models
from django.core.files.storage import FileSystemStorage
from mptt.fields import TreeForeignKey

from common.models.mixins import InfoModelMixin
from config.settings import MEDIA_ROOT

# Path to file storage
fs = FileSystemStorage(location=os.path.join(MEDIA_ROOT, 'fs'))

# User
User = get_user_model()


# Path to user files
def get_upload_path(instance, filename):
    return f'user_{instance.creator.id}/{filename}'


class File(InfoModelMixin):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,
                              related_name='files', verbose_name='Владелец', )
    file = models.FileField(verbose_name='Файл', null=False, blank=False,
                            upload_to=get_upload_path, storage=fs, )
    parent = TreeForeignKey(to='self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children', )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-created_at']

    def __str__(self):
        return self.file.name
