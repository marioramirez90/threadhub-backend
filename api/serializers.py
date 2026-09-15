from rest_framework import serializers
from .models import UserProfile, Post, Comment

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'isAdmin']
        read_only_fields = ['id']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'tags', 'createdAt', 'userId', 'upvotes', 'downvotes']
        read_only_fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'postId', 'userId', 'text', 'createdAt', 'upvotes', 'downvotes']
        read_only_fields = ['id']
