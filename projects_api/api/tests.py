from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from .models import Project, Tag
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the project model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.project_title = "Projects REST Apis"
        self.project_description = "REST Apis Projects Tracker App frontend"
        self.project = Project(title=self.project_title, description=self.project_description)

    def test_model_can_create_a_project(self):
        """Test the project model can create a project."""
        old_count = Project.objects.count()
        self.project.save()
        new_count = Project.objects.count()
        self.assertNotEqual(old_count, new_count)
        tag_one = Tag.objects.create(name="Python")
        tag_two = Tag.objects.create(name="Django")
        self.project.tags.add(tag_one, tag_two)
        self.project.save()
        self.assertEqual(self.project.tags.all().count(), 2)



class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        tag_one = Tag.objects.create(name="REST")
        tag_two = Tag.objects.create(name="APIs")
        self.client = APIClient()
        self.project_data = {'title': 'Jobs board App', 'description': 'A search engine for jobs seekers', 'started_at': '2016-03-01 08:00:00', 'tags': [tag_one.id, tag_two.id]}
        self.response = self.client.post(
            reverse('create-project'),
            self.project_data,
            format=None)

    def test_api_can_create_a_project(self):
        """Test the api has project creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)