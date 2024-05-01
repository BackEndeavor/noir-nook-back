from allauth.socialaccount.models import SocialAccount
from rest_framework import serializers

from authentication.models import NoirNookUser


class UserProfileSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = NoirNookUser
        fields = ['id', 'username', 'first_name', 'last_name', 'avatar_url']

    def get_avatar_url(self, obj):
        social_account = SocialAccount.objects.filter(user=obj).first()
        extra_data = social_account.extra_data
        return extra_data.get('avatar_url') or extra_data.get('picture')
