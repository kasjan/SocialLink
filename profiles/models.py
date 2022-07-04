import os
from SocialLink.settings import MEDIA_ROOT
from accounts.models import CustomUser as User
from django.db import models


class Social(models.Model):
    name = models.CharField(
        max_length=200,
    )
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        folder = f'{MEDIA_ROOT}/qr_codes'
        if not os.path.exists(folder):
            os.mkdir(folder)
        return super().save(*args, **kwargs)


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
