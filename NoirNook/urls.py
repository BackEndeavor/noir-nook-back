from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from NoirNook import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),
    path('api/auth/', include('authentication.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
