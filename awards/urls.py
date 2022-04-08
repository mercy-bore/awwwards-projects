from django.contrib.auth import views 
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
    re_path('accounts/', include('django_registration.backends.one_step.urls')),
    re_path('accounts/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    re_path(r'^new/post$', views.new_post, name='new-post'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^update/',app_views.update_profile,name='update_profile'),
    re_path('accounts/profile/',views.profile,name='profile'),
    re_path(r'^feeds_profile/(?P<pk>\d+)$',app_views.users_profile,name='users_profile'), 
    re_path(r'^post/(\d+)',views.detail,name ='detail'),
    










]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)