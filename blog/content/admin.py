from django.contrib import admin
from django.contrib.auth import get_user_model
from content.models import Post, PostComment

User = get_user_model()



class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']

class PostCommentAdmin(admin.ModelAdmin):
    search_fields = ['user__username']
    


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
# Register your models here.
