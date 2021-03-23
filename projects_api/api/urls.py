from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, TagGenericAPIView

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tags', TagGenericAPIView.as_view()),
]

urlpatterns += router.urls