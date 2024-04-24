from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from rest_framework.permissions import AllowAny


class GitHubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://localhost:5437/auth/callback/github'
    client_class = OAuth2Client


class GoogleConnect(SocialConnectView):
    permission_classes = [AllowAny]
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
