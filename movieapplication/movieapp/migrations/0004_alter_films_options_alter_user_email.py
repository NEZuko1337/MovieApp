# Generated by Django 4.2.5 on 2023-10-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_alter_user_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='films',
            options={'verbose_name_plural': 'Films'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
