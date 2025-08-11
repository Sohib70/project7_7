from django.shortcuts import render
from .models import CustomUser
from .serializers import RegisterSerilizers, LoginSerializers
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

class LoginApi(APIView):
    def post(self,request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            return Response({'data':serializer.validated_data,'status':status.HTTP_200_OK})
        return Response({'data': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

class LogoutApi(APIView):
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'msg':"Siz dasturdan chiqdingiz", 'status': status.HTTP_200_OK})
        except Exception as e:
            return Response({'error': e, 'status':status.HTTP_400_BAD_REQUEST})