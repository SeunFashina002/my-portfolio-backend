from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from .models import Projects, ProjectSlideshow, ProjectFunctionality, Stack
from .serializers import ProjectSerializer, SlideShowSerializer, FunctionalitySerializer, StackSerializer
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': '/projects/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of projects'
#         },
#         {
#             'Endpoint': '/project/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns a single project'
#         },
#     ]

#     return Response(routes)
@api_view(['GET'])
def getProjectStack(request, pk):
    try:
        project = Projects.objects.get(id=pk)
        stacks =  project.stack.all()
        serializer = StackSerializer(stacks, many=True)
        return Response(serializer.data)
    except Projects.DoesNotExist:
        return Response('Project does not exist', status=status.HTTP_404_NOT_FOUND)



    

@api_view(['GET'])
def getProjects(request):
    projects = Projects.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    try:
        project = Projects.objects.get(id=pk)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)
    except Projects.DoesNotExist:
        return Response('Project does not exist', status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getSlideShow(request, pk):
    try:
        image = ProjectSlideshow.objects.filter(project_id=pk)
        serializer = SlideShowSerializer(image, many=True)
        return Response(serializer.data)
    except ProjectSlideshow.DoesNotExist:
        return Response('Project does not exist', status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getFunctionality(request, pk):
    try:
        functionalities = ProjectFunctionality.objects.filter(project_id=pk)
        serializer = FunctionalitySerializer(functionalities, many=True)
        return Response(serializer.data)
    except ProjectFunctionality.DoesNotExist:
        return Response('Project does not exist', status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getStacks(request):
    stacks = Stack.objects.all()
    serializer = StackSerializer(stacks, many=True)
    return Response(serializer.data)



