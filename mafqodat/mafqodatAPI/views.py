from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from . import serializer

from .serializer import RegisterSerializer, LoginSetializer
from rest_framework import response, status,permissions




class AuthUserAPIView(GenericAPIView):
    authentication_classes = []

    primission_classes = (permissions.IsAuthenticated,)


    def get(self,request):
        user =request.user
        serializer =RegisterSerializer(user)
        return response.Response({'user':serializer.data})


class RergisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return response.Response(serializers.data, status=status.HTTP_201_CREATED)
        return response.Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIVeiw(GenericAPIView):
    authentication_classes = []
    serializer_class = LoginSetializer
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)
        if user:
            serializers = self.serializer_class(user)
            return response.Response(serializers.data, status=status.HTTP_200_OK)
        return response.Response({'message': "invalid credential, try again"}, status=status.HTTP_401_UNAUTHORIZED)


