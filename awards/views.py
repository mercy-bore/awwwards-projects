from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_signup(request):
    if request.method == 'POST':
        user_email = request.POST.get['email']
        username = request.POST.get['username']
        userpass = request.POST.get['password']
        try:
            user_obj = User.objects.create(username=username,email=user_email,password=userpass)
            user_obj.set_password(userpass)
            user_obj.save()
            user_auth = authenticate(username=username,password=userpass)
            login(request, user_auth)
            return redirect('home')
            
        except:
            messages.add_message(request,messages.ERROR,'Cannot signup')
            return render(request, 'signup.html')
    return render(request, 'signup.html')
            
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		userpass = request.POST['password']
		try:
			user_obj = authenticate(username=username, password=userpass)
			login(request, user_obj)
			request.session['username'] = username
			return redirect('home')
		except:
			messages.add_message(request, messages.ERROR, "Unable to log in.")
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')
def user_logout(request):
	try:
		logout(request)
		messages.add_message(request, messages.INFO, 'You\'re logged Out!')
	except:
		messages.add_message(request, messages.ERROR, "Unable to log out.")
	return redirect('home')