"""Serializers.py file."""
# 3rd-party
from rest_framework import serializers

# Project
from accounts.models import CustomUser as User

# Local
from .models import Link
from .models import Social


class SocialSerializer(serializers.ModelSerializer):  # noqa D101
    class Meta:  # noqa D106
        model = Social
        fields = [
            'url',
            'name',
            'icon',
        ]


class LinkSerializer(serializers.HyperlinkedModelSerializer):  # noqa D101
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field='username')
    social = serializers.SlugRelatedField(queryset=Social.objects.all(),
                                          slug_field='name')

    class Meta:  # noqa D106
        model = Link
        fields = [
            'url',
            'id',
            'social',
            'link',
            'user',
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):  # noqa D101
    link = serializers.HyperlinkedRelatedField(many=True,
                                               read_only=True,
                                               view_name='link-detail')

    class Meta:  # noqa D106
        model = User
        fields = [
            'id',
            'username',
            'email',
            'description',
            'link',
            'qr_code',
            'background',
            'photo',
            'views',
        ]
