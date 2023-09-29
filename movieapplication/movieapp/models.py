from django.db import models

class Films(models.Model):
    title = models.CharField(max_length=128, null=False)
    description = models.TextField(max_length=512, null = False)
    genre = models.CharField(max_length=32, null = False)
    photo = models.ImageField(null = False)
    actors = models.TextField(max_length=1024, blank=True)


    def __str__(self) -> str:
        return f'{self.title} | {self.genre}'