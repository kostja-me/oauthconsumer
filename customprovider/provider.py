from allauth.socialaccount.providers.base import ProviderAccount
from .views import CustomOAuth2Adapter
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class CustomAccount(ProviderAccount):
    def get_avatar_url(self):
        return self.account.extra_data.get("picture")


class CustomProvider(OAuth2Provider):
    id = "custom"
    name = "Custom"
    account_class = CustomAccount
    oauth2_adapter_class = CustomOAuth2Adapter

    def get_default_scope(self):
        return ['read', 'write']

    def extract_uid(self, data):
        return str(data["id"])

    def extract_common_fields(self, data):
        return dict(
            email=data.get("email"),
            last_name=data.get("familyName"),
            first_name=data.get("givenName"),
        )


provider_classes = [CustomProvider]
