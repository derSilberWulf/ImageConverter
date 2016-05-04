from django.db import models

# Create your models here.
class StoredImage(models.Model):
    image = models.ImageField()
    owner = models.ForeignKey('auth.User')
    