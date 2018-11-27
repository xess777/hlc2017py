# Generated by Django 2.1.3 on 2018-11-27 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_at', models.IntegerField(verbose_name='Время посещения timestamp')),
                ('mark', models.SmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Оценка')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.User')),
            ],
        ),
    ]