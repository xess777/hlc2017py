from django.db import models


class Visit(models.Model):
    location = models.ForeignKey(
        to='locations.Location', on_delete=models.PROTECT)
    user = models.ForeignKey(to='users.User', on_delete=models.PROTECT)
    visited_at = models.IntegerField(verbose_name='Время посещения timestamp')
    mark = models.SmallIntegerField(verbose_name='Оценка')
