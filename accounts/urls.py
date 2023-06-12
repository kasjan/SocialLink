"""Urls.py files."""
# Django
from django.urls import include
from django.urls import path
from django.urls import re_path

# 3rd-party
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(), name='account_confirm_email'),

]
