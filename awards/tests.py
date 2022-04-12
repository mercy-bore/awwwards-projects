from django.test import TestCase

# Create your tests here.
from .models import Post, Profile
from django.contrib.auth.models import User


# Create your tests here.
class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.profile = Profile(user=Profile(name='moringa'))
        self.profile.user.save()
        self.profile.save()
        self.post = Post(user=self.profile,photo='download.jpeg', title='pillaar', description='shanghai',url='http://heroku.com')
        self.post.save_post()
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.post, Post))     # Testing Save Method
    def test_save_image(self):
        self.post.save_project()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)
    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()
   
    
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = Profile(name='mercy')
        self.user.save()
        self.profile = Profile(id=1,user=self.user,profile_photo='download.jpeg',bio='Sofatware Dev', name='Mercy',contact='mercycherotich757@gmail.com')
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)