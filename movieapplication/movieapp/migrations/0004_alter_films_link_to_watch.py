# Generated by Django 4.2.5 on 2023-09-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_films_link_to_watch_films_planned_to_watch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='link_to_watch',
            field=models.TextField(blank=True, default='', max_length=512),
        ),
    ]
