from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Avg, Count





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
            
    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()
   
   
    
    def __str__(self):
        return "%s profile" % self.user


from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = HTMLField()
    photo = models.ImageField(upload_to='images/', default='default.png')
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=1)


    def __str__(self):
        return self.title
        
    def save_project(self):
        self.save()

    @classmethod
    def display_posts(cls):
        posts = cls.objects.all()
        return posts

   
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
   

    def delete_post(self):
        self.delete()


class ReviewRating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
    
    def save_review(self):
        self.save()
    def averageReview(self):
        reviews = ReviewRating.objects.filter(post=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(post=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score =models.IntegerField(default=0,
                               validators=[
                                   MaxValueValidator(5), 
                                   MinValueValidator(0),
                               ]
                               )
    def __str__(self):
        return str(self.pk)
