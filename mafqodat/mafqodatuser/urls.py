from django.urls import path
from .views import RegisterView_for_mobile, LoginAPIView_for_mobile, LogoutAPIView_for_mobile, \
    VerifyEmail_for_mobile, RequestPasswordResetEmail_for_mobile, PasswordTokenCheckAPI_for_mobile, \
    SetNewPasswordAPIView_for_mobile,  DeleteAccount_mobile
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [

    path('mobile/register', RegisterView_for_mobile.as_view(), name="register"),
    path('mobile/login', LoginAPIView_for_mobile.as_view(), name="login"),
    path('mobile/logout', LogoutAPIView_for_mobile.as_view(), name="logout"),
    path('mobile/email-verify', VerifyEmail_for_mobile.as_view(), name="email-verify"),
    path('mobile/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('mobile/<int:id>', DeleteAccount_mobile.as_view(), name="Delete_Email"),
    # path('mobile/request-reset-email', RequestPasswordResetEmail_for_mobile.as_view(),
    #     name="request-reset-email"),
    # path('mobile/password-reset/<uidb64>/<token>/',
    #     PasswordTokenCheckAPI_for_mobile.as_view(), name='password-reset-confirm'),
    # path('mobile/password-reset-complete', SetNewPasswordAPIView_for_mobile.as_view(),
    #     name='password-reset-complete')

]
