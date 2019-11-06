from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    quest         = models.CharField(max_length=200)
    description   = models.TextField(default="description will be soon")
    date_start    = models.DateTimeField(default=timezone.now)
    date_deadline = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.quest