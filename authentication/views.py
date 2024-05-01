from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from rest_framework.permissions import AllowAny


class GitHubConnect(SocialConnectView):
    callback_url = 'http://localhost:5437/auth/callback/github/'
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    permission_classes = [AllowAny]


class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    permission_classes = [AllowAny]
