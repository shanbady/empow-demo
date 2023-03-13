from django.test import TestCase,  RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
import os
from content.models import Post, PostComment

User = get_user_model()




class ContentTestCase(TestCase):


    def setUp(self):

        self.factory = RequestFactory()
        
        self.user = User.objects.create_superuser(
            username='test',
            email='test@gmail.com',
            password='password')

        self.post = Post.objects.create(
            title='test title',
            text='test blog text',
            author=self.user)

        self.comment = PostComment.objects.create(
            text='test blog commend',
            author=self.user,
            post = self.post)

    def tearDown(self):
        User.objects.all().delete()

    def test_post_is_not_destroyed_on_delete(self):
        post_count_initial = Post.objects.count()
        self.assertTrue(Post.objects.get(id=self.post.id).deleted == False)
        self.client.login(username=self.user.username, password='password')
        response = self.client.get('/posts/{post_id}/'.format(post_id=self.post.id), follow=True)
        self.assertTrue(response.status_code == 200)
        self.client.delete('/posts/{post_id}/'.format(post_id=self.post.id), follow=True)
        response = self.client.get('/posts/{post_id}/'.format(post_id=self.post.id), follow=True)
        self.assertTrue(response.status_code == 404)
        post_count_final = Post.objects.count()
        self.assertTrue(post_count_initial == post_count_final)
        self.assertTrue(Post.objects.get(id=self.post.id).deleted == True)

    def test_comment_is_not_destroyed_on_delete(self):
        comment_count_initial = PostComment.objects.count()
        self.assertTrue(PostComment.objects.get(id=self.comment.id).deleted == False)
        self.client.login(username=self.user.username, password='password')
        response = self.client.get('/comments/{comment_id}/'.format(comment_id=self.comment.id), follow=True)
        self.assertTrue(response.status_code == 200)
        self.client.delete('/comments/{comment_id}/'.format(comment_id=self.comment.id), follow=True)
        response = self.client.get('/comments/{comment_id}/'.format(comment_id=self.comment.id), follow=True)
        self.assertTrue(response.status_code == 404)
        comment_count_final = PostComment.objects.count()
        self.assertTrue(comment_count_initial == comment_count_final)
        self.assertTrue(PostComment.objects.get(id=self.comment.id).deleted == True)
