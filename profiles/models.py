from django.conf import settings
from django.db import models


class Social(models.Model):
    name = models.CharField(
        max_length=200,
    )
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Link(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    Social = models.ForeignKey(
        Social,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=True,
    )
    link = models.URLField(
        blank=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False)

    def __str__(self):
        return self.link
