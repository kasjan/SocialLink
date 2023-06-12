"""Views file."""
# Django
from django.shortcuts import get_object_or_404

# 3rd-party
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

# Project
from accounts.models import CustomUser as User

# Local
from .custompermissions import IsCurrentUserOwnerOrReadOnly
from .models import Link
from .models import Social
from .serializers import LinkSerializer
from .serializers import SocialSerializer
from .serializers import UserSerializer


# DRF views
class SocialList(generics.ListCreateAPIView):  # noqa D101
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    name = 'social-list'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class SocialDetail(generics.RetrieveUpdateDestroyAPIView):  # noqa D101
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    name = 'social-detail'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class LinkList(generics.ListCreateAPIView):  # noqa D101
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    name = 'link-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):  # noqa D101
        serializer.save(user=self.request.user)


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):  # noqa D101
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    name = 'link-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsCurrentUserOwnerOrReadOnly]


class UserLink(generics.ListAPIView):  # noqa D101
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class UserDetail(generics.RetrieveAPIView):  # noqa D101
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class ApiRoot(generics.GenericAPIView):  # noqa D101
    name = 'api-root'

    def get(self, request, *args, **kwargs):  # noqa D101
        return Response({'socials': reverse(SocialList.name, request=request),
                         'links': reverse(LinkList.name, request=request),
                         'users': reverse(UserLink.name, request=request)})


class ProfileView(APIView):  # noqa D101
    def get(self, request, username):   # noqa D101
        user = get_object_or_404(User, username__exact=username)
        user.views += 1
        user.save()

        queryset = Link.objects.filter(user__username__exact=username)
        serializer = LinkSerializer(queryset, many=True, context={'request': request})

        serializer_user = UserSerializer(user, context={'request': request})

        context = {
            'sites': serializer.data,
            'user': serializer_user.data,
        }

        return Response(context)
