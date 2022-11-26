from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    project_link = models.CharField(max_length=250, null=True, blank=True) 
    github_link = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stack = models.ManyToManyField('Stack')

    def __str__(self):
        return self.title

class Stack(models.Model):
    stack_name = models.CharField(max_length=50, null=True, blank=True)
    is_visible = models.BooleanField(default=True)
    stack_image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.stack_name

class ProjectSlideshow(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    alt = models.CharField(max_length=200, null=True, blank=True)

class ProjectFunctionality(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True)
    header = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(null=True, blank=True)
