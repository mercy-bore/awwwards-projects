from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    contact = models.EmailField(max_length=100, blank=True)
    
        
    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
        if created:
            Profile.objects.create(user = instance)


    def __str__(self):
        return "%s profile" % self.user



class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='images/', default='default.png')
    
    def __str__(self):
            return self.title
    def save_project(self):
        self.save()

    @classmethod
    def display_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def search_projects(cls,search_term):
        projects = cls.objects.filter(title__icontains = search_term).all()
        return projects

    def delete_post(self):
        self.delete()


