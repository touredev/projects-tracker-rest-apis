from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    """This class represents the project model."""
    DONE = 'DONE'
    IN_PROGRESS = 'IN_PROGRESS'
    TO_DO = 'TO_DO'
    STATUS_CHOICES = [
        (DONE, 'Done'),
        (IN_PROGRESS, 'In Progress'),
        (TO_DO, 'To Do'),
    ]

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000,blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TO_DO,
    )
    tags = models.ManyToManyField(Tag, blank=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', models.SET_NULL, related_name='projects', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)