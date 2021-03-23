from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import api_root, ProjectViewSet, TagGenericAPIView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'projects', ProjectViewSet, basename='projects')


urlpatterns = [
    path('', api_root),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("get-token/", obtain_auth_token),
    path('tags', TagGenericAPIView.as_view(), name="tags-list"),
]

urlpatterns += router.urls