from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

class Post(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instagram-home')
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()

    def get_all_images(cls):
        images = Image.objects.all()
        return images

    
class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    image_pic = models.ImageField(upload_to='posts/')
    image_name = models.CharField(max_length = 50)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)

    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'



    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
