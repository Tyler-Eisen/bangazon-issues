from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gimmeapi.models import User
from gimmeapi.serializers import UserSerializer

class UserView(ViewSet):
  
    def retrieve(self, request, pk):
      
        user= User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        data = serializer.data
        
        return Response(data)
    
    def list(self,request):
         
         users = User.objects.all()
         user = request.query_params.get('user', None)
         if user is not None:
             users = users.filter(user_id = user)
                  
         serializer = UserSerializer(users, many=True)
         return Response(serializer.data)
    def create(self, request):
        """POST request to create a rare user"""
        uid = request.data["uid"]
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=uid)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """PUT request to update a rare user"""
        user = User.objects.get(pk=pk)
        uid = request.data.get("uid", user.uid)
        name =  request.data.get("name", user.name)
        email =  request.data.get("email", user.email)
        address =  request.data.get("address", user.address)
        phone =  request.data.get("phone", user.phone)
        image_url =  request.data.get("imageUrl", user.image_url)
        user.uid = uid
        user.name = name
        user.email = email
        user.address = address
        user.phone = phone
        user.image_url = image_url
        user.save()
        return Response({'message': 'User Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to destroy a rare user"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message': 'User Destroyed'}, status=status.HTTP_204_NO_CONTENT)
