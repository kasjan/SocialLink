"""Models.py file."""
# Standard Library
import os

# Django
from django.db import models

# Project
from accounts.models import CustomUser as User
from SocialLink.settings import MEDIA_ROOT


class Social(models.Model):
    """Socials model."""

    name = models.CharField(
        max_length=200,
    )
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):  # noqa: D105
        return self.name

    def save(self, *args, **kwargs):  # noqa: D102
        folder = f'{MEDIA_ROOT}/qr_codes'
        if not os.path.exists(folder):
            os.mkdir(folder)
        return super().save(*args, **kwargs)


class Link(models.Model):
    """Users link model."""

    social = models.ForeignKey(
        Social,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    link = models.URLField(
        blank=False,
    )
    user = models.ForeignKey(
        User,
        related_name='link',
        on_delete=models.CASCADE,
        blank=False)

    def __str__(self):  # noqa: D105
        return self.link

    def save(self, *args, **kwargs):  # noqa: D102
        if Social.objects.filter(link__user=self.user):
            raise ValueError(f'{self.social} for {self.user} already exist.')
        return super().save(*args, **kwargs)
