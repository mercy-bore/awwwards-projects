from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    contact = models.EmailField(max_length=100, blank=True)
    
    
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()
        


class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(upload_to='images/', default='default.png')

