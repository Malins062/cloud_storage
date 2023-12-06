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


class InfoModelMixin(DateModelMixin):
    created_by = models.ForeignKey(
        User, models.SET_NULL,
        related_name='created_%(app_label)s_%(class)s',
        verbose_name='Кем создано', null=True, )
    updated_by = models.ForeignKey(
        User, models.SET_NULL,
        related_name='updated_%(app_label)s_%(class)s',
        verbose_name='Кем изменено', null=True, )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from crum import get_current_user

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        return super().save(*args, **kwargs)

