from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from content.serializers import PostSerializer, PostCommentSerializer
from content.models import Post, PostComment
from django.shortcuts import get_object_or_404


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.filter(deleted=False).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
    	instance.deleted = True
    	instance.save()

class PostCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PostComment.objects.filter(deleted=False).order_by('-created_at')
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
    	instance.deleted = True
    	instance.save()