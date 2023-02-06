from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .serializer import PostSerializer, Type_itemSerializer, PostForMobileSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Post, Type_item
from django_filters.rest_framework import DjangoFilterBackend


class PostAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['Name', 'location_id', 'phone_number']
    search_feilds = ['Name', 'location_id', 'phone_number']
    ordering_feilds = ['Name', 'location_id', 'phone_number']

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Post.objects.filter().values()


class Postfor_mobile_APIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostForMobileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['Name', 'location_id', 'type_id']
    search_feilds = ['Name', 'location_id', 'type_id']
    ordering_feilds = ['Name', 'location_id', 'type_id']

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Post.objects.defer("id", "Name", "location", "type_id", "image")


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Post.objects.filter()


class PostDetailAPIView_for_mobile(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Post.objects.defer("id", "Name", "location_id", "type_id", "image")


class Type_ItemAPIView(CreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = Type_itemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Type_item.objects.filter().values()


class Type_ItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = Type_itemSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Type_item.objects.filter()


@csrf_exempt
def SaveFile(request):
    file = request.FILES['image']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
