from rest_framework import serializers
from gimmeapi.models import Category

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""

    class Meta:
        model = Category
        fields = ('id', 
                  'name',)
        depth=2
