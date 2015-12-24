from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Forum(models.Model):
    them_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, blank=True)

    def __str__(self):
        return self.them_name

    class Meta:
        db_table = "forum_list"
        ordering = ["-date"]


class ExtendForum(models.Model):
    them_name = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum, default="Enot")
    user = models.ForeignKey(User, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.them_name

    class Meta:
        db_table = "ext_forum_list"
        ordering = ["-date"]


class ForumQuestion(models.Model):
    class Meta:
        db_table = "forum_questions"
