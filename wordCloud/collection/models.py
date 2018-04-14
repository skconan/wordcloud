from django.db import models

# Create your models here.
class Data(models.Model):
    id_data = models.CharField(max_length=30)
    data = models.CharField(max_length=256,blank=False)