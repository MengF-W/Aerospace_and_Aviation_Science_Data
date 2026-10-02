from django.db import models

# Create your models here.

from django.db import models

class APOD(models.Model):
  date = models.CharField(max_length=15)
  title = models.CharField(max_length=255)
  media_type = models.CharField(max_length=15)
  media_location = models.CharField(max_length=255)
  explanation = models.CharField(max_length=1024)
  credit = models.CharField(max_length=255)
  copyright = models.CharField(max_length=255)
  alt = models.CharField(max_length=500)
