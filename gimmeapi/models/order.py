from django.db import models
from .user import User

class Order(models.Model):
  buyer_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name='buyer_id', default=1)
  
  date = models.DateField(auto_now_add=True)
  shipped = models.BooleanField(default=False)
  payment_type = models.CharField(max_length=50)
  total = models.IntegerField()
  
