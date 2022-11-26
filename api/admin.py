from django.contrib import admin
from .models import Projects, Stack, ProjectSlideshow, ProjectFunctionality
# Register your models here.

admin.site.register(Projects)
admin.site.register(Stack)
admin.site.register(ProjectSlideshow)
admin.site.register(ProjectFunctionality)