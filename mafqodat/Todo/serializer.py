from rest_framework import serializers

from .models import Post, Type_item


class Type_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_item
        fields = ('id', 'name_type')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'Name','location','image','phone_number','By_user','Date','chat_count','Action','type_id')

        def get_Item_type(self):
            return Type_item.name_type


class PostForMobileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'Name','location','image','type_id')

        def get_Item_type(self):
            return Type_item.name_type




