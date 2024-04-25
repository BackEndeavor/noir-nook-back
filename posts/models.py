from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Post(Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    author_id = models.CharField(max_length=128)
    image_preview = models.ImageField(upload_to='posts/images', null=True, blank=True)
