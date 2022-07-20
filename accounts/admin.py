"""Admin file."""
# Django
from django.contrib import admin

# Project
from accounts.models import CustomUser

admin.site.register(CustomUser)
