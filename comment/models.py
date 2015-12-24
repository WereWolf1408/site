from django.db import models
from datetime import datetime
from publications.models import Publication
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["-date"]
        db_table = "comment"

    def __str__(self):
        return self.text