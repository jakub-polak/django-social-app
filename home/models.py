from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Friend(models.Model):
    user = models.ManyToManyField(User)
