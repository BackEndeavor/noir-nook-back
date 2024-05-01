from rest_framework import serializers

from authentication.serializer import UserProfileSerializer
from . import summarizer
from .models import Post

CONTENT_LIMIT_LENGTH = 256


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'image_preview', 'content', 'publication_date']


class PostListSerializer(PostSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'image_preview', 'content', 'publication_date']

    def get_content(self, obj):
        content = obj.content
        return content[:CONTENT_LIMIT_LENGTH].strip() + (content[CONTENT_LIMIT_LENGTH:] and '...')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_id', 'image_preview']
