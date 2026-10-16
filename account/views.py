from rest_framework.response import Response
from .serializer import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Register Compelete"},status=status.HTTP_201_CREATED)
    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    