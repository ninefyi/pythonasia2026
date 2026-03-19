
from django.db import models
from django_mongodb_backend.fields import ArrayField

class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot = models.TextField()
    # Vector field integration might vary, but standard ArrayField works for storage
    # The official backend documentation suggests using ArrayField for vectors.
    embedding = ArrayField(
        models.FloatField(),
        size=1024, # Dimension of voyage-4-large
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
