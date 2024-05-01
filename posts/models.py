from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

from NoirNook import settings


class Post(Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_preview = models.ImageField(upload_to='posts/images', null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
