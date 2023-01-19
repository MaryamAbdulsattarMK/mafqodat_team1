from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import Post
from .views import PostAPIView,PostDetailAPIView, SaveFile

urlpatterns = [
    path('Post',PostAPIView.as_view(),name='Post'),
    path('<int:id>', PostDetailAPIView.as_view(), name='Post_Detail'),
    path('save', SaveFile, name='Post_Detail')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)