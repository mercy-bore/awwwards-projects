from rest_framework import serializers
from .models import AwwwardProjects

class AwwwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwwwardProjects
        fields = ('id','title','url','description')

