from django.contrib import admin
from .models import Social
from .models import Link

admin.site.register(Social)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'user')


admin.site.register(Link, LinkAdmin)



