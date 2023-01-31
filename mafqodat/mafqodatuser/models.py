from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Permission
from django.db import models

# Create your models here.
from rest_framework_simplejwt.tokens import  AccessToken

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'twitter': 'twitter', 'email': 'email'}


class MyUserManager_for_mobile(BaseUserManager):
    def create_user_for_mobile(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user_for_mobile = self.model(username=username, email=self.normalize_email(email))
        user_for_mobile.set_password(password)
        user_for_mobile.save()
        return user_for_mobile


class myUser_for_mobile(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))

    # EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = MyUserManager_for_mobile()

    def __str__(self):
        return self.email

    def token(self):
        refresh = AccessToken.for_user(self)
        return {

            'access': str(refresh)
        }
