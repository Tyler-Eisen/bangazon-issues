from django.db import models
from .order import Order
from .product import Product

class OrderItem(models.Model):
  order_id= models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_id',default=1)
  
  product_id= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id',default=1)

  quantity = models.IntegerField()
  
