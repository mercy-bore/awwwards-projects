from . import views
from django.urls import re_path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    re_path(r'^$',views.home,name = 'home'),
    re_path('signup/', views.user_signup, name='signup'),
	re_path('login/', views.user_login, name='login'),
	re_path('logout/', views.user_logout, name='logout'),

]