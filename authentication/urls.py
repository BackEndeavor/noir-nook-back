from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import UserDetailsView
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from authentication.views import GoogleConnect, GitHubConnect

urlpatterns = [
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path('google/', GoogleConnect.as_view(), name='google_oauth'),
    path('github/', GitHubConnect.as_view(), name='github_oauth')
]
