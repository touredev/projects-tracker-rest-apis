from django.urls import path
from .views import ProjectGenericAPIView, TagGenericAPIView


urlpatterns = [
    path('projects', ProjectGenericAPIView.as_view(), name="create-project"),
    path('tags', TagGenericAPIView.as_view()),

]