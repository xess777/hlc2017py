from django.db import models


class Location(models.Model):
    place = models.TextField(verbose_name='Описание достопримечательности')
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    distance = models.PositiveIntegerField(verbose_name='Расстояние от города')
