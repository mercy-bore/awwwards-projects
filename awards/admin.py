from django.contrib import admin
from .models import Profile,Post,ReviewRating,Rating
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(ReviewRating)
admin.site.register(Rating)