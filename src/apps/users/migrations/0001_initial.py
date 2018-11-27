# Generated by Django 2.1.3 on 2018-11-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('gender', models.SmallIntegerField(choices=[(1, 'm'), (2, 'f')], verbose_name='Пол')),
                ('birth_date', models.IntegerField(verbose_name='Дата рождения timestamp')),
            ],
        ),
    ]
