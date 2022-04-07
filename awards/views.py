from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from . forms import Registration,UpdateUser,UpdateProfile,postProjectForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from .models import Profile,Post
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
import os

# Create your views here.
def home(request):
    projects = Post.display_posts()
    return render(request, 'home.html',{"posts": projects})

def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('registration/login.html')
  else:
    form = Registration()
  return render(request,'registration/registration_form.html',{"form":form})

@login_required
def post(request):
  if request.method == 'POST':
    post_form = postProjectForm(request.POST,request.FILES) 
    if post_form.is_valid():
      the_post = post_form.save(commit = False)
      the_post.user = request.user
      the_post.save()
      return redirect('home')

  else:
    post_form = postProjectForm()
  return render(request,'post.html',{"post_form":post_form})

@login_required
def profile(request):
  current_user = request.user
  posts = Post.objects.all()
  user_photos = Post.objects.filter(user_id = current_user.id).all()
  
  return render(request,'profile/profile.html',{"posts":posts,'user_photos':user_photos,"current_user":current_user})

def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = postProjectForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = current_user
            article.save()
        return redirect('home')

    else:
        form = postProjectForm()
    return render(request, 'new_article.html', {"form": form})
