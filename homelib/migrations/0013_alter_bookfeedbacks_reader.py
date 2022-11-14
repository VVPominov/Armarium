# Generated by Django 4.1.2 on 2022-10-29 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homelib', '0012_bookfeedbacks_reader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfeedbacks',
            name='reader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Читатель'),
        ),
    ]
