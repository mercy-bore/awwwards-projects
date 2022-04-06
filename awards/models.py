from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    contact = models.EmailField(max_length=100, blank=True)
class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(upload_to='images/', default='default.png')

