from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Tag
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the project model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jeantoure")
        self.project_title = "Projects REST Apis"
        self.project_description = "REST Apis Projects Tracker App frontend"
        self.project = Project(title=self.project_title, description=self.project_description, owner=user)

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
        user = User.objects.create(username="jeantoure")
        tag_one = Tag.objects.create(name="REST")
        tag_two = Tag.objects.create(name="APIs")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.project_data = {'title': 'Jobs board App', 'description': 'A search engine for jobs seekers', 'started_at': '2016-03-01 08:00:00', 'tags': [tag_one.id, tag_two.id], 'owner': user.id}
        self.response = self.client.post(
            reverse('projects-list'),
            self.project_data,
            format="json")

    def test_api_can_create_a_project(self):
        """Test the api has project creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get(reverse('projects-detail', kwargs={'pk': 3}),
            format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_project(self):
        """Test the api can get a given project."""
        project = Project.objects.get()
        response = self.client.get(
            reverse('projects-detail',
            kwargs={'pk': project.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, project)

    def test_api_can_update_project(self):
        """Test the api can update a given project."""
        project = Project.objects.get()
        change_project = {'title': 'New project', 'description': 'New description'}
        res = self.client.put(
            reverse('projects-detail', kwargs={'pk': project.id}),
            change_project, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)

    def test_api_can_delete_project(self):
        """Test the api can delete a project."""
        project = Project.objects.get()
        response = self.client.delete(
            reverse('projects-detail', kwargs={'pk': project.id}),
            format="json",
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)