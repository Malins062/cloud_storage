import os
from django.contrib.auth import get_user_model
from django.db import models
from django.core.files.storage import FileSystemStorage
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from common.models.mixins import InfoModelMixin
from config.settings import MEDIA_ROOT
from storage.models.folders import Folder

# Path to file storage
fs = FileSystemStorage(location=os.path.join(MEDIA_ROOT, 'fs'))

# User
User = get_user_model()


# Path to user files
def get_upload_path(instance, filename):
    return f'user_{instance.created_by.id}/{filename}'


class File(InfoModelMixin, MPTTModel):
    # owner = models.ForeignKey(to=User, on_delete=models.CASCADE,
    #                           null=False, blank=False,
    #                           related_name='user', verbose_name='Владелец', )
    file = models.FileField(verbose_name='Файл', null=False, blank=False,
                            upload_to=get_upload_path, storage=fs, )
    parent = TreeForeignKey(to=Folder, on_delete=models.CASCADE,
                            null=True, blank=True, related_name='folder', )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-created_at']

    class MPTTMeta:
        order_insertion_by = ['file']

    def __str__(self):
        return self.file.name
