# Generated by Django 4.1.2 on 2022-10-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homelib', '0008_alter_genres_name_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='definition',
            field=models.CharField(default=' ', max_length=300, verbose_name='Краткое описание'),
        ),
    ]
