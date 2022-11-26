from django.urls import path
from .views import getRoutes, getProjects, getProject

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('projects/', getProjects, name='projects'),
    path('projects/<str:pk>', getProject, name='projects'),

]
