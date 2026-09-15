import time
import uuid
from django.db import models

def current_time_ms():
    return int(time.time() * 1000)

def generate_uuid():
    return str(uuid.uuid4())

class UserProfile(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=generate_uuid, editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, default='')
    password = models.CharField(max_length=128)
    isAdmin = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        ordering = ['username']

    def __str__(self):
        return self.username

class Post(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=generate_uuid, editable=False)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, default='')
    tags = models.JSONField(default=list, blank=True)
    createdAt = models.BigIntegerField(default=current_time_ms)
    userId = models.CharField(max_length=64)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        db_table = 'posts'
        ordering = ['-createdAt']

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=generate_uuid, editable=False)
    postId = models.CharField(max_length=64)
    userId = models.CharField(max_length=64)
    text = models.TextField()
    createdAt = models.BigIntegerField(default=current_time_ms)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        db_table = 'comments'
        ordering = ['createdAt']

    def __str__(self):
        return f'Comment {self.id} on Post {self.postId}'
