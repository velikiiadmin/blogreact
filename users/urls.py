from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('logout/blacklist/', BlackListToken.as_view(), name='blacklist'),
]