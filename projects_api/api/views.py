# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ProjectSerializer, TagSerializer
from .models import Project, Tag


class TagGenericAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TagSerializer(queryset, many=True)
        
        return Response({
            'data': serializer.data
        })

    def perform_create(self, serializer):
        """Save the post data when creating a new tag."""
        serializer.save()

        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

class ProjectGenericAPIView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProjectSerializer(queryset, many=True)
        
        return Response({
            'data': serializer.data
        })

    def perform_create(self, serializer):
        """Save the post data when creating a new project."""
        serializer.save()

        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)