from rest_framework import viewsets
from .models import UserProfile, Post, Comment
from .serializers import UserProfileSerializer, PostSerializer, CommentSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = None

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Post.objects.all()
        user_id = self.request.query_params.get('userId')
        if user_id:
            queryset = queryset.filter(userId=user_id)
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.request.query_params.get('postId')
        if post_id:
            queryset = queryset.filter(postId=post_id)
        user_id = self.request.query_params.get('userId')
        if user_id:
            queryset = queryset.filter(userId=user_id)
        return queryset
