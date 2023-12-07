from django.contrib.auth import get_user_model
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from common.models.mixins import InfoModelMixin

# User
User = get_user_model()


class Folder(InfoModelMixin, MPTTModel):
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='folders', verbose_name='Владелец'
    )
    name = models.CharField(verbose_name='Наименование', max_length=255, blank=False, null=False, )
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
