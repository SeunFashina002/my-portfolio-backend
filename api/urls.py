from django.urls import path
from .views import getProjects, getProject, getSlideShow, getFunctionality, getStacks, getProjectStack

urlpatterns = [
    # path('', getRoutes, name='routes'),
    path('stacks/', getStacks, name='stack'),
    path('projects/', getProjects, name='projects'),
    path('projects/<str:pk>', getProject, name='project'),
    path('projects/<str:pk>/detail/slideshows', getSlideShow, name='slideshow'),
    path('projects/<str:pk>/detail/pstack', getProjectStack, name='project_stack'),
    path('projects/<str:pk>/detail/functionality', getFunctionality, name='functionality'),


]
