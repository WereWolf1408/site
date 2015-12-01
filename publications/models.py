from django.db import models
from datetime import datetime


class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000, blank=True)
    image_source = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title