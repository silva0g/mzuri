from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='artist_logo/', blank=False)

    def __str__(self):
        return self.name
