from .models import Accont
from .seralizer import AccontSerializer
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class AccontView(APIView):
    def get(self,request):
        data = Accont.objects.all()
        serializer = AccontSerializer(data,many=True)
        return Response(serializer.data)
    def post(self,request):
        
        serializer = AccontSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccontDetailView(APIView):
    
    def get(self,request,pk):
        data = Accont.objects.get(id=pk)
        serializer = AccontSerializer(data,many=True)
        return Response(serializer.data)
    def put(self,request,pk):
        data = Accont.objects.get(id=pk)
        serializer = AccontSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk):
            data = Accont.objects.get(id=pk)
            data.delete()
            return Response({"message":"Product Deleted"})


@api_view(['GET'])
def get_profile(request,pk):
    data = get_object_or_404(Accont,id=pk)
    serializer =AccontSerializer(data)
    return Response(serializer.data)
@api_view(['POST'])
def add_coin(request,pk):
    data = get_object_or_404(Accont,id=pk)

