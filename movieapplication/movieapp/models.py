from django.db import models
from django.contrib.auth.models import AbstractUser

class Films(models.Model):
    title = models.CharField(max_length=128, null=False)
    description = models.TextField(max_length=512, null = False)
    genre = models.CharField(max_length=32, null = False)
    photo = models.ImageField(null = False, upload_to='films_page')
    actors = models.TextField(max_length=1024, blank=True)
    link_to_watch = models.TextField(max_length=512, null=False, default='', blank=True)
    watched = models.BooleanField(null=False, default=False)
    planned_to_watch = models.BooleanField(null=False, default=False)

    class Meta:
        verbose_name_plural = 'Films'

    def __str__(self) -> str:
        return f'{self.title} | {self.genre}'
    

class User(AbstractUser):
    photo = models.ImageField(blank=True, upload_to='profile_photos')
    email = models.EmailField(null=False, unique=True)
    
