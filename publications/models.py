from django.db import models
from django.db.models import Count
from datetime import datetime


# create my manager
class MyManager(models.Manager):
    pass


class BookMarks(models.Manager):
    def get_queryset(self):
        return super(BookMarks, self).get_queryset().filter(bookmark=True)

    def bookmark_count(self):
        return Publication.get_bookmarks.count()


class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000, blank=True)
    image_source = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    bookmark = models.BooleanField(blank=False)
    objects = models.Manager()
    get_bookmarks = BookMarks()

    class Meta:
        ordering = ["-date"]
        db_table = "publication"

    def __str__(self):
        return self.title