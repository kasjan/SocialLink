from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Social, Link
from .serializers import SocialSerializer
from .serializers import LinkSerializer
from .serializers import UserSerializer


class SocialList(generics.ListCreateAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    name = 'social-list'


class SocialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    name = 'social-detail'


class LinkList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    name = 'link-list'


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    name = 'link-detail'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserLink(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
