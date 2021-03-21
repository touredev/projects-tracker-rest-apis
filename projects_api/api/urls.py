from django.urls import path
from rest_framework import routers
from .views import ProjectViewSet, TagGenericAPIView

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('tags', TagGenericAPIView.as_view()),
]

urlpatterns += router.urls