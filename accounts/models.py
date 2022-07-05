from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from profiles.utils import qr_code_generator
from django.contrib.auth.models import PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email missing")
        if not username:
            raise ValueError("nickname missing")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
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

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.qr_code = qr_code_generator(self.username)
        return super().save(*args, **kwargs)
