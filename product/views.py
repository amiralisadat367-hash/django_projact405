
from rest_framework.response import Response 
from rest_framework.decorators import (api_view ,permission_classes)
from .models import Product
from .serializera import ProductSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 
from rest_framework.permissions import IsAuthenticated ,AllowAny

class Product_list(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class Product_Retrieve(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 
@api_view(['GET'])
def get_search(request):
    search = request.query_params.get('search')
    data = Product.objects.filter(name__icontains=search).order_by('id')
    serializer = ProductSerializer(data,many=True)
    return Response({"data":serializer.data})
    







