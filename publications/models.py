from django.db import models
from datetime import datetime


# create my manager
class MyManager(models.Manager):
    pass


class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000, blank=True)
    image_source = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    objects = models.Manager()
    public = MyManager()

    class Meta:
        ordering = ["-date"]
        db_table = "publication"

    def __str__(self):
        return self.title