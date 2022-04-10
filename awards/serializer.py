from rest_framework import serializers
from .models import Post,Profile,User

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','url','description','photo','user')
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','profile_photo','bio','name','contact')
class UserSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = User
        fields = ['id',  'username', 'email']


