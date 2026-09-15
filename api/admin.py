from django.contrib import admin
from .models import UserProfile, Post, Comment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'isAdmin', 'id')
    search_fields = ('username', 'email')
    list_filter = ('isAdmin',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'userId', 'createdAt', 'upvotes', 'downvotes')
    search_fields = ('title', 'text')
    list_filter = ('createdAt',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'postId', 'userId', 'createdAt', 'upvotes', 'downvotes')
    search_fields = ('text',)
