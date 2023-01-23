from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import Post
from .views import PostAPIView, PostDetailAPIView, SaveFile, Type_ItemDetailAPIView, Type_ItemAPIView, \
    Postfor_mobile_APIView

urlpatterns = [
    path('Post',PostAPIView.as_view(),name='Post'),
    path('<int:id>', PostDetailAPIView.as_view(), name='Post_Detail'),
    path('Type_item_create', Type_ItemAPIView.as_view(), name='Post_Detail'),
    path('Type_item_Update', Type_ItemDetailAPIView.as_view(), name='Post_Detail'),
    path('Post_M', Postfor_mobile_APIView.as_view(), name='Post_Detail'),


    path('save', SaveFile, name='Post_Detail')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)