from insta.models import Comment, Image, Post
from django.contrib import admin

# Register your models here.

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Image)