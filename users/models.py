from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinLengthValidator
from django.db import models

from users.manager import CustomUserManager


class CustomUser(AbstractUser):
    """"Моделька для Кастомного пользователя"""
    username = None
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(6)], unique=True)
    balance = models.PositiveBigIntegerField( default=10)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Кастомные Пользователи'
        verbose_name = 'Кастомный пользователь'