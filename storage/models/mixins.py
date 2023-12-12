from django.contrib.auth import get_user_model
from django.db import models

# User
User = get_user_model()


class InfoEntityModelMixin(models.Model):
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name='Владелец',
    )
    name = models.CharField(verbose_name='Наименование', max_length=255, blank=False, null=False, )
    description = models.TextField(verbose_name='Описание', blank=True, null=True, )

    class Meta:
        abstract = True
