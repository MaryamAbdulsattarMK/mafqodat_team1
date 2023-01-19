from django.urls import path
from .views  import RergisterAPIView,LoginAPIVeiw,AuthUserAPIView

urlpatterns = [
    path('register', RergisterAPIView.as_view(),name="register"),
    path('login', LoginAPIVeiw.as_view(), name="Login"),
    path('user',AuthUserAPIView.as_view(),name='user'),





]