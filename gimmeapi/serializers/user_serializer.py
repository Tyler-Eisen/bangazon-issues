from rest_framework import serializers
from gimmeapi.models import User

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = User
        fields = ('id', 
                  'uid', 
                  'name',
                  'email', 
                  'address', 
                  'phone', 
                  'image_url', )
        depth = 2
