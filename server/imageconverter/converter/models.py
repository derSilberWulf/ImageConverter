from django.db import models

# Create your models here.
class StoredImage(models.Model):
    image = models.ImageField(upload_to='database')
    owner = models.ForeignKey('auth.User')
    
    def delete(self, *args, **kwargs):
        """
        The image stored in the filesystem
        should also be deleted
        """
        self.image.delete()
        super(StoredImage, self).delete(*args, **kwargs)
        