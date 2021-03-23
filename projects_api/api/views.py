# Create your views here.
from rest_framework import generics, status, viewsets, permissions
from .permissions import IsOwner
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

    def post(self, request):
        return Response({
            'data': self.create(request).data
        }, status=status.HTTP_201_CREATED)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def list(self, request):
        serializer = ProjectSerializer(Project.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(project)

        return Response({
            'data': serializer.data
        })

    def update(self, request, pk=None):
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(instance=project, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        