from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gimmeapi.models import Order, User
from gimmeapi.serializers import OrderSerializer

class OrderView(ViewSet):
    def retrieve(self, request, pk):
        # Retrieve the Order instance
        order = Order.objects.get(pk=pk)

        # Serialize the Order instance
        serializer = OrderSerializer(order)
        data = serializer.data

        return Response(data)
      
    def list(self, request):
      orders = Order.objects.all()
      buyer_id = request.query_params.get('buyer_id', None)
      if buyer_id is not None:
        orders = orders.filter(buyer_id=buyer_id)

      serializer = OrderSerializer(orders, many=True)
      return Response(serializer.data)
    
    def create(self, request):
      buyer_id = request.data["buyer_id"]
      serializer = OrderSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save(buyer_id_id=buyer_id)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
      """PUT request to update an order"""
      order = Order.objects.get(pk=pk)
      
      buyer_id = request.data.get("buyer_id", order.buyer_id_id)
      shipped = request.data.get("shipped", order.shipped)
      payment_type = request.data.get("payment_type", order.payment_type)
      total = request.data.get("total", order.total)
      
      order.buyer_id_id = buyer_id
      order.shipped = shipped
      order.payment_type = payment_type
      order.total = total
      order.save()
      
      return Response({'message': 'Order Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
      """DELETE request to destroy an order"""
      order = Order.objects.get(pk=pk)
      order.delete()
      return Response({'message': 'Order Destroyed'}, status=status.HTTP_204_NO_CONTENT)
