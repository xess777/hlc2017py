from django.db import models

from .enums import GenderEnum


class User(models.Model):
    email = models.EmailField(verbose_name='email', max_length=100)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    gender = models.SmallIntegerField(
        verbose_name='Пол', choices=GenderEnum.get_choices())
    birth_date = models.IntegerField(verbose_name='Дата рождения timestamp')
