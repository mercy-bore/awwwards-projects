from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from . forms import Registration,UpdateUser,UpdateProfile,postProjectForm,ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from .models import Profile,Post,ReviewRating,Rating
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
import os
#!............API/djangorestframework  imports>>>>>>>>>>>>
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  AwwwardProjects
from .serializer import ProjectSerializer,ProfileSerializer,UserSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets





# Create your views here.

# ! start of API views **************************



class ProjectList(APIView):
    def get(self, request,format=None):
        projects = Post.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ProjectSerializer(post,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
      
class ProfileList(APIView):
    def get(self, request,format=None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ProfileSerializer(post,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
      
class UserList(APIView):
    def get(self, request,format=None):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = UserSerializer(post,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return AwwwardProjects.objects.get(pk=pk)
        except AwwwardProjects.DoesNotExist:
            return Http404
    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)
      
    def put(self, request, pk, format=None):
            project = self.get_project(pk)
            serializers = ProjectSerializer(project, request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)      
    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      
      # ********************* end of API views *********************
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

@login_required(login_url='/accounts/login/')
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
  user_photos = Post.objects.filter(id = current_user.id).all()
  
  return render(request,'profile/profile.html',{"posts":posts,'user_photos':user_photos,"current_user":current_user})

@login_required(login_url='/accounts/login/')
def new_post(request):
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
    return render(request, 'new_post.html', {"form": form})
  
def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        projects = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def users_profile(request,pk):
  user = User.objects.get(pk = pk)
  projects = Post.objects.filter(user = user)
  c_user = request.user
  
  return render(request,'profile/users_profile.html',{"user":user,"projects":projects,"c_user":c_user})

def update_profile(request):
  if request.method == 'POST':
    user_form = UpdateUser(request.POST,instance=request.user)
    profile_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    user_form = UpdateUser(instance=request.user)
    profile_form = UpdateProfile(instance=request.user.profile) 
  params = {'user_form':user_form,'profile_form':profile_form}
  return render(request,'profile/update.html',params)

def detail(request,post_id):
  current_user = request.user
  try:
    post = get_object_or_404(Post, pk = post_id)
    reviews = ReviewRating.objects.filter(pk=post_id, status=True)

  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'post_detail.html', {'post':post,'current_user':current_user,'reviews':reviews})

def rating(request,post):
  ratings = Rating.objects.filter(user=request.user, post=post).first()
  rating_status = None
  if ratings is None:
        rating_status = False
  else:
        rating_status = True
        if request.method == 'POST':
          form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Rating.objects.filter(post=post)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
        else:
            form = ReviewForm()
        params = {
            'post': post,
            'rating_form': form,
            'rating_status': rating_status

        }
        return render(request, 'post_detail.html',params, {'post':post})

def submit_review(request, post_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, post__id=post_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.post_id = post_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)

# def submit_review(request,post_id):
#   url = request.META.get("HTTP_REFERER")
#   if request.method == 'POST':
#     try:
#       reviews = ReviewRating.objects.get(user__id=request.user.id,post__id=post_id)
#       form = ReviewForm(request.POST,instance=reviews)
#       form.save()
#       messages.success(request,'Thanks  your review has been updated.')
#       return redirect(url)
      
      
#     except ReviewRating.DoesNotExist :
#       form = ReviewForm(request.POST)
#       if form.is_valid():
#         data = ReviewRating()
#         data.subject = form.cleaned_data['subject']
#         data.review = form.cleaned_data['review']
#         data.rating = form.cleaned_data['rating']
#         data.ip = request.META.get("REMOTE_ADDR")
#         data.post_id =post_id
#         data.user_id = request.user_id
#         data.save()
#         messages.success(request,'Thanks for your feedback!')
#         return redirect('')