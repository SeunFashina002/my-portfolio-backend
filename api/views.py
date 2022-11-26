from django.shortcuts import render
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/projects/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of projects'
        },
        {
            'Endpoint': '/project/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single project'
        },
    ]

    return Response(routes)

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
    except:
        pass
    return Response('Data does not exist')

