from rest_framework import serializers
from blog.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'image', 'author', 'excerpt', 'content', 'status', 'slug')
        model = Post
