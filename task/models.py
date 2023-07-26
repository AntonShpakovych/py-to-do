from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "created_at"]

    def __str__(self):
        return self.content[:10] + "..."
