from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import Post
from .views import PostAPIView, PostDetailAPIView, SaveFile, Type_ItemDetailAPIView, Type_ItemAPIView, \
    Postfor_mobile_APIView, PostDetailAPIView_for_mobile, PostTimeDetailAPIView, PostTimeDetail_for_mobileAPIView, \
    PostTimeDetailAPIView_id, PostTimeDetailAPIView_for_mobile,RegionAPIViewUP,RegionAPIView

urlpatterns = [
    path('admin/Post',PostAPIView.as_view(),name='Post'),
    path('admin/Post/<int:id>', PostDetailAPIView.as_view(), name='Post_Detail'),
    path('admin/Type_item/create', Type_ItemAPIView.as_view(), name='Post_Detail'),
    path('admin/Type_item/<int:id>', Type_ItemDetailAPIView.as_view(), name='Post_Detail'),
    path('admin/Post_History', PostTimeDetailAPIView.as_view(), name='Post_History'),
    path('admin/Post_History/<int:id>', PostTimeDetailAPIView_id.as_view(), name='Post_History'),
    path('admin/Region', RegionAPIViewUP.as_view(), name='RegionAPIView'),
    path('admin/Region/<int:id>', RegionAPIView.as_view(), name='Region'),



    path('mobile/Type_item/create', Type_ItemAPIView.as_view(), name='Post_Detail'),
    path('mobile/Type_item/Update/<int:id>', Type_ItemDetailAPIView.as_view(), name='Post_Detail'),
    path('mobile/Post', Postfor_mobile_APIView.as_view(), name='Post_Detail'),
    path('mobile/Post/<int:id>', PostDetailAPIView_for_mobile.as_view(), name='Post_Detail'),
    path('mobile/Post_History', PostTimeDetail_for_mobileAPIView.as_view(), name='Post_History'),
    path('mobile/Post_History/<int:id>',  PostTimeDetailAPIView_for_mobile.as_view(), name='Post_History'),
    path('mobile/Region', RegionAPIViewUP.as_view(), name='RegionAPIView'),
    path('mobile/Region/<int:id>', RegionAPIView.as_view(), name='Region'),




    path('save', SaveFile, name='Post_Detail')





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)