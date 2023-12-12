from django.contrib.auth import get_user_model
from django.db import models

# User
User = get_user_model()


class InfoEntityModelMixin(models.Model):
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name='Владелец',
    )
    description = models.TextField(verbose_name='Описание', blank=True, null=True, )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from crum import get_current_user
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.owner = user
        return super().save(*args, **kwargs)