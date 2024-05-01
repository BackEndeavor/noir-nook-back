from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView

from NoirNook.pagination import StandardResultsPagination
from .models import Post
from .serializer import PostSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = StandardResultsPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer


@api_view(['GET'])
def test(request):
    return HttpResponse(f'Request authentication state: {request.user.username}')
