from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'
#
# router = DefaultRouter()
# router.register('', PostList, basename='posts')
# urlpatterns = router.urls
urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<str:pk>/', PostDetail.as_view(), name='postdetail'),
    path('search/', PostListDetailFilter.as_view(), name='search'),
    path('admin/create/', AdminPostUpload.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
