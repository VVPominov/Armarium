# Generated by Django 4.1.2 on 2022-10-30 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homelib', '0019_alter_bookfeedbacks_options_alter_cities_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='definition',
            new_name='description',
        ),
    ]
