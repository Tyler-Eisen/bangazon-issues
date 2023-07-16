from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    address= models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    image_url = models.CharField(max_length=1000, default=1)
