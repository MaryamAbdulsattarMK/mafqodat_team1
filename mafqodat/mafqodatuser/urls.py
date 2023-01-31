from django.urls import path
from .views import  RegisterView_for_mobile, LoginAPIView_for_mobile, LogoutAPIView_for_mobile, \
    VerifyEmail_for_mobile, RequestPasswordResetEmail_for_mobile, PasswordTokenCheckAPI_for_mobile, \
    SetNewPasswordAPIView_for_mobile
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [

    path('register_mobile_user/', RegisterView_for_mobile.as_view(), name="register"),
    path('login__mobile_user/', LoginAPIView_for_mobile.as_view(), name="login"),
    path('logout__mobile_user/', LogoutAPIView_for_mobile.as_view(), name="logout"),
    path('email-verify__mobile_user/', VerifyEmail_for_mobile.as_view(), name="email-verify"),
    path('token/refresh_mobile_user/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('request-reset-email_mobile_user/', RequestPasswordResetEmail_for_mobile.as_view(),
    #     name="request-reset-email"),
    # path('password-reset_mobile_user/<uidb64>/<token>/',
    #     PasswordTokenCheckAPI_for_mobile.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete_mobile_user', SetNewPasswordAPIView_for_mobile.as_view(),
    #     name='password-reset-complete')

]
