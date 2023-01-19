from rest_framework import  serializers
from .models import myUser


class RegisterSerializer(serializers.ModelSerializer):

    password =  serializers.CharField(
        max_length = 128,min_length = 6, write_only=True )

    class Meta():
        model = myUser
        fields = ('username','email','password')

    def create(self,validated_data):
        return myUser.objects.create_user(**validated_data)


class LoginSetializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,min_length=6,write_only=True
    )

    class Meta:
        model= myUser
        fields =('email','password','token')

        read_only_fields = ['token']



