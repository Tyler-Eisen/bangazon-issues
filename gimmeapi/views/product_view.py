from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gimmeapi.models import Product, User, Category
from gimmeapi.serializers import ProductSerializer

class ProductView(ViewSet):
  
    def retrieve(self, request, pk=None):
      
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def list(self, request):
         
        products = Product.objects.all()
        category = request.query_params.get('category', None)
        if category is not None:
            products = products.filter(category_id=category)
        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def create(self, request):
      """POST request to create a Product"""
      category_id = request.data["category_id"]
      seller_id = request.data["seller_id"]
      name = request.data["name"]
      price = request.data["price"]
      description = request.data["description"]
      stock = request.data["stock"]
      image_url = request.data["image_url"]

      try:
          category = Category.objects.get(id=category_id)
      except Category.DoesNotExist:
          return Response({"error": "Category with this ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

      try:
          seller = User.objects.get(id=seller_id)
      except User.DoesNotExist:
          return Response({"error": "Seller with this ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

      data = {
          'category_id': category.id,
          'seller_id': seller.id,
          'name': name,
          'price': price,
          'description': description,
          'stock': stock,
          'image_url': image_url
      }

      serializer = ProductSerializer(data=data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
