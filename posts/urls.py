from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts import views
from posts.views import PostViewSet

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('test', views.test)
]
