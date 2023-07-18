from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from gimmeapi.models import Category
from gimmeapi.serializers import CategorySerializer

class CategoryView(ViewSet):
  
    def list(self, request):
        """Handle GET requests to get all Categories
      
        Returns:
            Response -- JSON serialized list of Categories
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk=None):
        """Handle GET requests for single Category

        Returns:
            Response -- JSON serialized Category instance
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exist.'}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        """Handles POST requests for new Category

        Returns:
            Response -- JSON serialized Category instance
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """Handle PUT requests for a Category

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exist.'}, status=status.HTTP_404_NOT_FOUND)
          
    def destroy(self, request, pk=None):
        """Handles DELETE requests for a single Category

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exist.'}, status=status.HTTP_404_NOT_FOUND)
