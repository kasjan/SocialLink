from django.contrib.auth.models import User
from django.db import models


class Social(models.Model):
    name = models.CharField(
        max_length=200,
    )
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Link(models.Model):
    social = models.ForeignKey(
        Social,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    link = models.URLField(
        blank=False
    )
    user = models.ForeignKey(
        User,
        related_name='link',
        on_delete=models.CASCADE,
        blank=False)

    def __str__(self):
        return self.link
