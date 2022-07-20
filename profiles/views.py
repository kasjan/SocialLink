"""Views file."""
# Django
from django.shortcuts import render

# 3rd-party
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Project
from accounts.models import CustomUser as User

# Local
from .custompermissions import IsCurrentUserOwnerOrReadOnly
from .models import Link
from .models import Social
from .serializers import LinkSerializer
from .serializers import SocialSerializer
from .serializers import UserSerializer


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsCurrentUserOwnerOrReadOnly]


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


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'socials': reverse(SocialList.name, request=request),
                         'links': reverse(LinkList.name, request=request),
                         'users': reverse(UserLink.name, request=request)})


def profile_view(request, username):
    if User.objects.filter(username__exact=username):
        counter = User.objects.get(username__exact=username)
        counter.views = counter.views + 1
        counter.save()
    queryset = Link.objects.filter(user__username__exact=username)
    try:
        desc = User.objects.get(username__exact=username)
    except User.DoesNotExist:
        desc = None
    context = {
        'object_list': queryset,
        'user': desc,
    }

    return render(request, 'user.html', context)
