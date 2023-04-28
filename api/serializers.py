from dataclasses import field
from operator import mod
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Projects, ProjectSlideshow, ProjectFunctionality, Stack

from django.conf import settings

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = '__all__'

    def get_image(self, obj):
        image_url = obj.image.url
        full_url = f"{settings.BASE_URL}/static{image_url}"
        return full_url

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = self.get_image(instance)
        return data

        
    
class SlideShowSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = ProjectSlideshow
        fields = '__all__'

    def get_image(self, obj):
        image_url = obj.image.url
        full_url = f"{settings.BASE_URL}/static{image_url}"
        return full_url

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = self.get_image(instance)
        return data


class FunctionalitySerializer(ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = ProjectFunctionality
        fields = '__all__'


    def get_images(self, obj):
        image_url = obj.images.url
        full_url = f"{settings.BASE_URL}/static{image_url}"
        return full_url

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = self.get_images(instance)
        return data

class StackSerializer(ModelSerializer):
    stack_image = serializers.SerializerMethodField()
    class Meta:
        model = Stack
        fields = '__all__'


    def get_stack_image(self, obj):
        image_url = obj.stack_image.url
        full_url = f"{settings.BASE_URL}/static{image_url}"
        return full_url

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = self.get_stack_image(instance)
        return data
