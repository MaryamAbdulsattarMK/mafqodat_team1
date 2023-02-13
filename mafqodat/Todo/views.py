from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .serializer import PostSerializer, Type_itemSerializer, PostForMobileSerializer, PostDetailSerialzer, \
    PostDetailSerialzer_for_mobile, RegionSerialzere
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Post, Type_item, PostTimeDetail
from django_filters.rest_framework import DjangoFilterBackend






class RegionAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = RegionSerialzere
    lookup_field = 'id'

    def get_queryset(self):
        return Post.objects.filter()


class RegionAPIViewUP(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = RegionSerialzere


    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Post.objects.filter()





class queryPostTimeDetailAPIView_for_mobile(CreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostDetailSerialzer_for_mobile

    def get_queryset(self):
        return PostTimeDetail.objects.filter('')


class PostAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['Name', 'location', 'phone_number','is_checked_by_admin']
    search_feilds = ['Name', 'location', 'phone_number','is_checked_by_admin']
    ordering_feilds = ['Name', 'location', 'phone_number','is_checked_by_admin']

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Post.objects.filter()


class Postfor_mobile_APIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostForMobileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['Name', 'location', 'type_id','is_checked_by_admin']
    search_feilds = ['Name', 'location', 'type_id','is_checked_by_admin']
    ordering_feilds = ['Name', 'location', 'type_id','is_checked_by_admin']

    def perform_create(self, serializer):
        #queryPostTimeDetailAPIView_for_mobile('http://127.0.0.1:8000/api/admin/Post_History')
        return serializer.save()

    def get_queryset(self):
        return Post.objects.filter()



class PostTimeDetailAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostDetailSerialzer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['created_at','updated_at']
    search_feilds = ['created_at','updated_at']
    ordering_feilds = ['created_at','updated_at']


    def get_queryset(self):
        return PostTimeDetail.objects.defer("id", 'created_at','updated_at')


class PostTimeDetail_for_mobileAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostDetailSerialzer_for_mobile
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['created_at','updated_at']
    search_feilds = ['created_at','updated_at']
    ordering_feilds = ['created_at','updated_at']

    def get_queryset(self):
        return PostTimeDetail.objects.defer("id", 'created_at','updated_at')


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
        return Post.objects.defer("id", "Name", "location", "type_id", "image",'PostDetail')




class PostTimeDetailAPIView_id(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostDetailSerialzer
    lookup_field = 'id'

    def get_queryset(self):
        return PostTimeDetail.objects.filter()
class PostTimeDetailAPIView_for_mobile(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostDetailSerialzer_for_mobile
    lookup_field = 'id'

    def get_queryset(self):
        return PostTimeDetail.objects.filter()






class Type_ItemAPIView(CreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = Type_itemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Type_item.objects.filter()


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

