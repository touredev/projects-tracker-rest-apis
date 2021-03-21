from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)