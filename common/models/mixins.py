from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime


# User
User = get_user_model()


class BaseInstanceStorageModel(models.Model):
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(default=datetime.now, verbose_name='Дата изменения')

    class Meta:
        abstract = True
