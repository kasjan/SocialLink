"""Admin.py file."""
# Django
from django.contrib import admin

# Local
from .models import Link
from .models import Social

admin.site.register(Social)


class LinkAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = ('user', 'social', 'link')


admin.site.register(Link, LinkAdmin)
