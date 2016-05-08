from django.db import models
import os

class StoredImage(models.Model):
    """
    A model for storing images
    """
    image = models.ImageField(upload_to='database')
    owner = models.ForeignKey('auth.User')
    
    def delete(self, *args, **kwargs):
        """
        The image stored in the filesystem
        should also be deleted
        """
        self.image.delete()
        super(StoredImage, self).delete(*args, **kwargs)
    def __unicode__(self):
        return os.path.basename(self.image.path)
        