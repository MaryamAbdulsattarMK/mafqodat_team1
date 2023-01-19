from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'Name','location','image','phone_number','By_user','Date','chat_count','Action')



