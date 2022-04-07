from . import views
from django.urls import re_path,include,path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views as app_views
urlpatterns=[
    re_path(r'^$',views.home,name = 'home'),
    path('accounts/register/',app_views.register,name='register'),
    path('',auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),


 

]