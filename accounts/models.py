"""Models file."""
# Django
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Project
from profiles.utils import qr_code_generator


class AccountManager(BaseUserManager):  # noqa: D101
    def create_user(self, email, username, password=None):
        """Create user."""
        if not email:
            raise ValueError('email missing')
        if not username:
            raise ValueError('nickname missing')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """Create user with all permissions."""
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""

    email = models.EmailField(unique=True)
    description = models.TextField(max_length=100, default='Default description')
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    views = models.IntegerField(
        default=0,
        null=True,
        blank=True)
    background = models.ImageField(upload_to='user_backgrounds/', blank=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountManager()

    def __str__(self):  # noqa: D105
        return self.username

    def save(self, *args, **kwargs):  # noqa: D102
        if not self.qr_code:
            self.qr_code = qr_code_generator(self.username)
        return super().save(*args, **kwargs)
