from django.db import models
import os
from django.conf import settings
from django.db.models.fields import CharField
from django.contrib.auth.models import User
# from django.views.generic.list import T
class Hotel (models.Model):
    chooseIMG = models.ImageField(upload_to='images/')
    def __str__(self):
        return (str(self.chooseIMG))
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.chooseIMG))
        super(Hotel,self).delete(*args,**kwargs)
