from _operator import sub
from operator import add

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from django.utils import timezone
from .models import Post, Type_item, location, PostTimeDetail, Region


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class Type_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_item
        fields = ('id', 'name_type')


class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = ('id', 'City','address', 'latitude' ,'longitude')


class PostDetailSerialzer(serializers.ModelSerializer):
    #created_at = PostTimeDetail(read_only = True, default = timezone.now)
    edits_time=serializers.SerializerMethodField()

    class Meta:
        model = PostTimeDetail
        ordering = ('-created_at',)
        fields = ( 'created_at', 'updated_at', 'expierd_at', 'edits_time')
    def get_edits_time(self, obj):
        return add(obj.edits_time,1)



class PostSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    PostDetail= PostDetailSerialzer()
    image = Base64ImageField(required=False)
    class Meta:
        model = Post
        fields = ('id', 'Name','location','image','phone_number','Date','chat_count','Action','type_id','is_checked_by_admin','PostDetail')

        def get_Item_type(self):
            return Type_item.name_type







class PostDetailSerialzer_for_mobile(serializers.ModelSerializer):
    edits_time=serializers.SerializerMethodField()
    class Meta:
        model = PostTimeDetail
        ordering = ('-created_at',)
        fields = ( 'created_at', 'updated_at', 'expierd_at', 'edits_time')

    def get_edits_time(self, obj):
        return add(obj.edits_time,1)

class PostForMobileSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    PostDetail = PostDetailSerialzer_for_mobile()
    image= Base64ImageField(required=False)
    class Meta:
        model = Post
        fields = ('id', 'Name','location','image','type_id','is_checked_by_admin','PostDetail')

        def get_Item_type(self):
            return Type_item.name_type






class RegionSerialzere(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('id','city','Region')








