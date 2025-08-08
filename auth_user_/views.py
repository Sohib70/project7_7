from django.shortcuts import render
from .models import CustomUser
from .serializers import RegisterSerilizers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.

class RegisterApi(APIView):
    def post(self,request):
        serializer = RegisterSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,'status':status.HTTP_201_CREATED})
        return Response({'message':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})