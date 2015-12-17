from django.db import models


class Forum(models.Model):
    them_name = models.CharField(max_length=100)

    def __str__(self):
        return self.them_name


class ExtendForum(models.Model):
    ext_them_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ext_them_name


class ExtendForumQuestion(models.Model):
    pass
