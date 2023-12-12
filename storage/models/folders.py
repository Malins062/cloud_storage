from django.contrib.auth import get_user_model
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from common.models.mixins import DateModelMixin
from storage.models.mixins import InfoEntityModelMixin

# User
User = get_user_model()


class Folder(InfoEntityModelMixin,
             DateModelMixin,
             MPTTModel):
    parent = TreeForeignKey(to='self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children', )

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        super(Folder, self).save(*args, **kwargs)
        Folder.objects.rebuild()

    def __str__(self):
        return self.name
