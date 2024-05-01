from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, PostSummarizeView

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/<pk>', PostSummarizeView.as_view())
]
