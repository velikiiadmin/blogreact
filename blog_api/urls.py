from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='posts')
urlpatterns = router.urls
