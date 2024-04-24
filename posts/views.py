from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Post
from .serializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def test(request):
    return HttpResponse(f'Request authentication state: {request.user.username}')
