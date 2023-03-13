from django.contrib.auth import get_user_model
from rest_framework import serializers
from content.models import Post, PostComment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'created_at', 'modified_at', 'url']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'author', 'created_at', 'modified_at', 'url']