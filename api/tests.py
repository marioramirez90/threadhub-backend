from django.test import TestCase
from rest_framework.test import APIClient
from api.models import UserProfile, Post, Comment

class ThreadHubAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            id='test-user-uuid-1',
            username='Testinand',
            email='testinand@test.de',
            password='password123',
            isAdmin=False
        )
        self.post = Post.objects.create(
            id='test-post-uuid-1',
            title='Test Post Title',
            text='Test Post Content text',
            tags=['TestTag', 'Django'],
            createdAt=1667606819000,
            userId=self.user.id,
            upvotes=5,
            downvotes=1
        )
        self.comment = Comment.objects.create(
            id='test-comment-uuid-1',
            postId=self.post.id,
            userId=self.user.id,
            text='A nice comment',
            createdAt=1667606820000,
            upvotes=1,
            downvotes=0
        )

    def test_get_users_list_without_slash(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['username'], 'Testinand')

    def test_get_user_detail(self):
        response = self.client.get(f'/users/{self.user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], 'Testinand')
        self.assertEqual(response.json()['isAdmin'], False)

    def test_get_posts_list_without_slash(self):
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)
        posts = response.json()
        self.assertIsInstance(posts, list)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], 'Test Post Title')
        self.assertEqual(posts[0]['tags'], ['TestTag', 'Django'])
        self.assertIsInstance(posts[0]['createdAt'], int)

    def test_create_post_without_trailing_slash(self):
        new_post_payload = {
            'title': 'New Vue Created Post',
            'text': 'Some insightful text',
            'tags': ['New', 'Vue'],
            'createdAt': 1726000000000,
            'userId': self.user.id,
            'upvotes': 0,
            'downvotes': 0
        }
        response = self.client.post('/posts', new_post_payload, format='json')
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['title'], 'New Vue Created Post')
        self.assertEqual(data['tags'], ['New', 'Vue'])
        self.assertTrue('id' in data and len(data['id']) > 0)

    def test_update_post_put(self):
        updated_payload = {
            'id': self.post.id,
            'title': 'Updated Post Title',
            'text': 'Updated Content',
            'tags': ['Edited'],
            'createdAt': self.post.createdAt,
            'userId': self.post.userId,
            'upvotes': 10,
            'downvotes': 2
        }
        response = self.client.put(f'/posts/{self.post.id}', updated_payload, format='json')
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post Title')
        self.assertEqual(self.post.text, 'Updated Content')

    def test_delete_post(self):
        response = self.client.delete(f'/posts/{self.post.id}')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_get_and_create_comment(self):
        response = self.client.get('/comments')
        self.assertEqual(response.status_code, 200)
        comments = response.json()
        self.assertEqual(len(comments), 1)

        new_comment = {
            'postId': self.post.id,
            'userId': self.user.id,
            'text': 'Second comment',
            'createdAt': 1726000050000,
            'upvotes': 0,
            'downvotes': 0
        }
        response = self.client.post('/comments', new_comment, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.filter(postId=self.post.id).count(), 2)

    def test_cors_headers(self):
        response = self.client.get('/posts', HTTP_ORIGIN='http://localhost:5173')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access-control-allow-origin', response.headers)
