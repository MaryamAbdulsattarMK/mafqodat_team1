from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .serializer import PostSerializer, Type_itemSerializer, PostForMobileSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from django_filters.rest_framework import DjangoFilterBackend


class PostAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['Name','location','phone_number']
    search_feilds = ['Name','location','phone_number']
    ordering_feilds = ['Name','location','phone_number']

    def perform_create(self,serializer):
        return serializer.save()

    def get_queryset(self):
        return Post.objects.filter()


class Postfor_mobile_APIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostForMobileSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['Name','location','type_id']
    search_feilds = ['Name','location','type_id']
    ordering_feilds = ['Name','location','type_id']

    def perform_create(self,serializer):
        return serializer.save()

    def get_queryset(self):
        return Post.objects.filter


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Post.objects.filter()




class Type_ItemAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = Type_itemSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['id','name_type']
    search_feilds = ['id','name_type']
    ordering_feilds = ['id','name_type']

    def perform_create(self,serializer):
        return serializer.save()

    def get_queryset(self):
        return Post.objects.filter()


class Type_ItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = Type_itemSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Post.objects.filter()




@csrf_exempt
def SaveFile(request):
    file = request.FILES['image']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)