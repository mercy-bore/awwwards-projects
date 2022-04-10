from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Post,ReviewRating,Rating
from django.contrib.auth.models import User


# registering user
class Registration(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username','email','password1','password2']


    # user post class

class postProjectForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','url','description','photo']


class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_photo','bio']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']