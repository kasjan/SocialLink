"""Tests.py file."""
# Django
from django.core.files.uploadedfile import SimpleUploadedFile

# 3rd-party
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# Local
from . import views
from .models import Social


class SocialTests(APITestCase):
    def post_social(self, name, icon):
        url = reverse(views.SocialList.name)
        data = {'name': name,
                'icon': icon, }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_social(self):
        new_social_name = 'Github'
        new_social_icon = SimpleUploadedFile('icon.jpg', b"file_content",
                                             content_type='image/jpg')
        response = self.post_social(new_social_name, new_social_icon)
        assert response.status_code == status.HTTP_201_CREATED
        assert Social.objects.count() == 1
        assert Social.objects.get().name == new_social_name
