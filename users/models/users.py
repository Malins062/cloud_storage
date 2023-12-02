from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from users.models.managers import CustomUserManager


class User(AbstractUser):
    phone_number = PhoneNumberField(verbose_name='Телефон', unique=True, null=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
