import rest_framework_simplejwt
from rest_framework import generics, status, views, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import DjangoModelPermissions

from .serializer import RegisterSerializer_for_mobile, \
    EmailVerificationSerializer_for_mobile, LoginSerializer_for_mobile, ResetPasswordEmailRequestSerializer_for_mobile, \
    SetNewPasswordSerializer_for_mobile, LogoutSerializer_for_mobile, ExpensesSerializer_mobile
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import  myUser_for_mobile

import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from django.http import HttpResponsePermanentRedirect
import os


from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.email == request.user



class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']

# for mobile


class RegisterView_for_mobile(generics.GenericAPIView):
    serializer_class = RegisterSerializer_for_mobile
    #renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = myUser_for_mobile.objects.get(email=user_data['email'])


        #Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail_for_mobile(views.APIView):
    serializer_class = EmailVerificationSerializer_for_mobile

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = myUser_for_mobile.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView_for_mobile(generics.GenericAPIView):
    serializer_class = LoginSerializer_for_mobile

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail_for_mobile(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer_for_mobile

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if myUser_for_mobile.objects.filter(email=email).exists():
            user = myUser_for_mobile.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://' + current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                         absurl + "?redirect_url=" + redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            #Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI_for_mobile(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer_for_mobile

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = myUser_for_mobile.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url + '?token_valid=False')
                else:
                    return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(
                    redirect_url + '?token_valid=True&message=Credentials Valid&uidb64=' + uidb64 + '&token=' + token)
            else:
                return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return CustomRedirect(redirect_url + '?token_valid=False')

            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView_for_mobile(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer_for_mobile

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class LogoutAPIView_for_mobile(generics.GenericAPIView):
    serializer_class = LogoutSerializer_for_mobile

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteAccount_mobile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer_mobile
    permission_classes = [DjangoModelPermissions]

    queryset = myUser_for_mobile.objects.all()
    lookup_field = "id"

    def get_queryset(self):

        return self.queryset.filter()# super(AccountInstance, self).delete(request, *args, **kwargs)


