from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import Post
from .views import PostAPIView, PostDetailAPIView, SaveFile, Type_ItemDetailAPIView, Type_ItemAPIView, \
    Postfor_mobile_APIView, PostDetailAPIView_for_mobile

urlpatterns = [
    path('admin/Post',PostAPIView.as_view(),name='Post'),
    path('admin/Post/<int:id>', PostDetailAPIView.as_view(), name='Post_Detail'),
    path('admin/Type_item/create', Type_ItemAPIView.as_view(), name='Post_Detail'),
    path('admin/Type_item/Update/<int:id>', Type_ItemDetailAPIView.as_view(), name='Post_Detail'),
    path('mobile/Type_item/create', Type_ItemAPIView.as_view(), name='Post_Detail'),
    path('mobile/Type_item/Update/<int:id>', Type_ItemDetailAPIView.as_view(), name='Post_Detail'),
    path('mobile/Post', Postfor_mobile_APIView.as_view(), name='Post_Detail'),
    path('mobile/Post/<int:id>', PostDetailAPIView_for_mobile.as_view(), name='Post_Detail'),
    path('save', SaveFile, name='Post_Detail')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)