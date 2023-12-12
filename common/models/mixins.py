from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

# User
User = get_user_model()


class DateModelMixin(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', null=True, blank=True, default=None, )
    updated_at = models.DateTimeField(verbose_name='Дата изменения', null=True, blank=True, default=None, )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateModelMixin, self).save(*args, **kwargs)
