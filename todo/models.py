from django.db import models


# Create your models here.
class Todo(models.Model):
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
