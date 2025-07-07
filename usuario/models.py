from django.db import models

class Usuario(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    thumbnail_url = models.URLField(max_length=300)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
