from rest_framework import serializers
from gimmeapi.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for order items"""
    class Meta:
        model = OrderItem
        fields = ('id', 
                  'order_id', 
                  'product_id', 
                  'quantity',)
        depth = 2
