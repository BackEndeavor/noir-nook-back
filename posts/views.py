from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from NoirNook.pagination import StandardResultsPagination
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializer import PostSerializer, PostListSerializer, PostSummarizeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = StandardResultsPagination
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer


class PostSummarizeView(mixins.RetrieveModelMixin, GenericAPIView):
    serializer_class = PostSummarizeSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
