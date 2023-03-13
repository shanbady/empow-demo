from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

'''
Create a dockerised Django/PSQL project for a simple blog with comments (model and API without UI part).
Post including Author, Title, Text, Date fields
Comment is connected to the post and has Author, Text, Date fields
Important: both the post and comments should have a soft delete feature. Please think on how to make this on Django and API side.
'''

class BasePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Post(BasePost):
    title = models.CharField(max_length=255, blank=False, null=False)
	

class PostComment(BasePost):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   
   
   