from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gimmeapi.models import OrderItem
from gimmeapi.serializers import OrderItemSerializer

class OrderItemView(ViewSet):
  
    def retrieve(self, request, pk):
      
        order_item = OrderItem.objects.get(pk=pk)
        serializer = OrderItemSerializer(order_item)
        data = serializer.data
        
        return Response(data)
    
    def list(self, request):
         
      order_items = OrderItem.objects.all()
      order = request.query_params.get('order', None)
      if order is not None:
          order_items = order_items.filter(order_id=order)
                  
      serializer = OrderItemSerializer(order_items, many=True)
      return Response(serializer.data)
  
    def create(self, request):
        """Handle POST request to create an OrderItem"""
        order_id = request.data["order_id"]
        product_id = request.data["product_id"]
        quantity = request.data["quantity"]
        data = {
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity
        }

        serializer = OrderItemSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, pk=None):
        """PUT request to update an OrderItem"""
        order_item = OrderItem.objects.get(pk=pk)
        order_item.product_id = request.data["product_id"]
        order_item.order_id = request.data["order_id"]
        order_item.quantity = request.data["quantity"]
        
        order_item.save()

        serializer = OrderItemSerializer(order_item, context={'request': request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """DELETE request to delete an OrderItem"""
        try:
            order_item = OrderItem.objects.get(pk=pk)
            order_item.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except OrderItem.DoesNotExist as ex:
            return Response({'message': str(ex)}, status=status.HTTP_404_NOT_FOUND)
