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
        id = request.query_params.get('seller', None)
        print('products for id:', id)
        if id is not None:
            products = products.filter(seller_id=id)
            print(f'found {len(products)} product(s)')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    
    def create(self, request):
        seller = User.objects.get(pk=request.data["seller"])
        categories = Category.objects.filter(id__in=request.data.get("categories", []))

        product = Product(
            seller=seller,
            name=request.data["name"],
            description=request.data["description"],
            stock=request.data["stock"],
            image_url=request.data["image_url"]
        )
        product.save()
        product.category.set(categories)

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a product
            
        Returns:
            Response -- JSON serialized updated Product instance
        """
        product = Product.objects.filter(pk=pk).first()
        product.name = request.data.get("name", product.name)
        product.price = request.data.get("price", product.price)
        product.description = request.data.get("description", product.description)
        product.stock = request.data.get("stock", product.stock)
        product.image_url = request.data.get("image_url", product.image_url)

        seller_id = request.data.get("seller", product.seller_id)
        seller = User.objects.get(pk=seller_id)
        product.seller = seller

        # Update the many-to-many relationship with categories
        category_ids = request.data.get("category", [])
        categories = Category.objects.filter(id__in=category_ids)
        product.category.set(categories)

        product.save()

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
