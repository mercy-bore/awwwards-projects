from django.contrib import admin
from .models import Profile,Post,ReviewRating
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(ReviewRating)