from rest_framework import generics
from django.contrib.auth.models import User
from .models import Social, Link
from .serializers import SocialSerializer
from .serializers import LinkSerializer
from .serializers import UserSerializer
from rest_framework import permissions
from .custompermissions import IsCurrentUserOwnerOrReadOnly


class SocialList(generics.ListCreateAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    name = 'social-list'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class SocialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    name = 'social-detail'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class LinkList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    name = 'link-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    name = 'link-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly]


class UserLink(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
