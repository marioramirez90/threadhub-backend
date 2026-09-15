import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import UserProfile, Post, Comment

class Command(BaseCommand):
    help = 'Seeds initial users, posts, and comments from db.json'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, default=None, help='Path to db.json file')
        parser.add_argument('--clear', action='store_true', help='Clear existing data before seeding')

    def handle(self, *args, **options):
        file_path = options['file']
        if not file_path:
            default_path = Path(settings.BASE_DIR) / 'db.json'
            if default_path.exists():
                file_path = str(default_path)
            else:
                alt_path = Path(settings.BASE_DIR).parent / 'final-project-2024-05-threadhub-api' / 'db.json'
                file_path = str(alt_path)

        if not Path(file_path).exists():
            self.stderr.write(self.style.ERROR(f'Datei {file_path} nicht gefunden!'))
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if options['clear']:
            Comment.objects.all().delete()
            Post.objects.all().delete()
            UserProfile.objects.all().delete()
            self.stdout.write(self.style.WARNING('Bestehende Daten wurden geloescht.'))

        # Seed Users
        users_count = 0
        for user_data in data.get('users', []):
            obj, created = UserProfile.objects.update_or_create(
                id=user_data['id'],
                defaults={
                    'username': user_data['username'],
                    'email': user_data.get('email', ''),
                    'password': user_data['password'],
                    'isAdmin': user_data.get('isAdmin', False),
                }
            )
            users_count += 1

        # Seed Posts
        posts_count = 0
        for post_data in data.get('posts', []):
            obj, created = Post.objects.update_or_create(
                id=post_data['id'],
                defaults={
                    'title': post_data['title'],
                    'text': post_data.get('text', ''),
                    'tags': post_data.get('tags', []),
                    'createdAt': post_data.get('createdAt', 0),
                    'userId': post_data['userId'],
                    'upvotes': post_data.get('upvotes', 0),
                    'downvotes': post_data.get('downvotes', 0),
                }
            )
            posts_count += 1

        # Seed Comments
        comments_count = 0
        for comment_data in data.get('comments', []):
            obj, created = Comment.objects.update_or_create(
                id=comment_data['id'],
                defaults={
                    'postId': comment_data['postId'],
                    'userId': comment_data['userId'],
                    'text': comment_data['text'],
                    'createdAt': comment_data.get('createdAt', 0),
                    'upvotes': comment_data.get('upvotes', 0),
                    'downvotes': comment_data.get('downvotes', 0),
                }
            )
            comments_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Erfolgreich initialisiert: {users_count} Benutzer, {posts_count} Posts, {comments_count} Kommentare.'
        ))
