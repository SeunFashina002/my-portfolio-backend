from dataclasses import field
from operator import mod
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Projects, ProjectSlideshow, ProjectFunctionality, Stack

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        
    
class SlideShowSerializer(ModelSerializer):
    class Meta:
        model = ProjectSlideshow
        fields = '__all__'

class FunctionalitySerializer(ModelSerializer):
    class Meta:
        model = ProjectFunctionality
        fields = '__all__'

class StackSerializer(ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'