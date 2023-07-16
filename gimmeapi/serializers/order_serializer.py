from rest_framework import serializers
from gimmeapi.models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id', 
            'buyer_id',
            'date',
            'shipped',
            'payment_type',
            'total',
        )
        depth = 2
