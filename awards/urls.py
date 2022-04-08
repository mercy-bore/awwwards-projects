from . import views
from django.urls import re_path,include,path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django_registration.backends.one_step.views import RegistrationView
from . import views as app_views
from django.conf.urls.static import static


urlpatterns=[
    re_path(r'^$',views.home,name = 'home'),
    path('accounts/register/',app_views.register,name='register'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
    path('accounts/register/',
        RegistrationView.as_view(success_url='accounts/login/'),
        name='django_registration_register'),
        
    re_path(r'^new/post$', views.new_post, name='new-post'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)