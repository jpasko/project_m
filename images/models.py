from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(default='', max_length=140)
    image = models.ImageField(upload_to='images/')
