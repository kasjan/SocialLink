from rest_framework import generics
from accounts.models import CustomUser as User
from .models import Social, Link
from .serializers import SocialSerializer
from .serializers import LinkSerializer
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
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


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'socials': reverse(SocialList.name, request=request),
                         'links': reverse(LinkList.name, request=request),
                         'users': reverse(UserLink.name, request=request)})
