
from rest_framework.response import Response 
from rest_framework.decorators import api_view ,APIView
from .models import Product
from .serializera import ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView
# @api_view(['GET','POST'])
# def all(request):
#     if request.method == "GET":
#         data =  Product.objects.all()
#         serializer = ProductSerializer(data,many = True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         # data = request.data
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def get_detail(request,pk):
#     data =  get_object_or_404(Product,id = pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(data)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(data,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         data.delete()
#         return Response({"message":status.HTTP_202_ACCEPTED})
        
# class Product_list(APIView):
#     def get(self,request):
#         data =  Product.objects.all()
#         serializer = ProductSerializer(data,many = True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class Product_details(APIView):
#     def get(self,request,pk):
#         data =  get_object_or_404(Product,id = pk)
#         serializer = ProductSerializer(data)
#         return Response(serializer.data)

#     def put(self,request,pk):
#         data = get_object_or_404(Product,id=pk)
#         serializer = ProductSerializer(data,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         data = get_object_or_404(Product,id=pk)
#         data.delete()
#         return Response({"message":"Product Deleted"})
class Product_list(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def get_search(request):
    search = request.query_params.get('search')
    data = Product.objects.filter(name__icontains=search).order_by('id')
    serializer = ProductSerializer(data,many=True)
    return Response({"data":serializer.data})
    







