# Generated by Django 4.1.2 on 2022-10-29 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homelib', '0015_remove_libraries_city_libraries_library_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libbooks',
            name='library',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homelib.libraries', verbose_name='Домашняя библиотека'),
        ),
        migrations.AddField(
            model_name='libraries',
            name='library_reader',
            field=models.OneToOneField(default='2', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
