# Generated by Django 4.2.5 on 2023-09-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='photo',
            field=models.ImageField(upload_to='films_page'),
        ),
    ]
