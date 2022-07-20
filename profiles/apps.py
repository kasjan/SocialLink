"""Apps.py file."""
# Django
from django.apps import AppConfig


class ProfilesConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
