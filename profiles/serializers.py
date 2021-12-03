from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Social
from .models import Link


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = [
            'url',
            'name',
            'icon'
        ]


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    social = serializers.SlugRelatedField(queryset=Social.objects.all(), slug_field='name')

    class Meta:
        model = Link
        fields = [
            'url',
            'id',
            'social',
            'link',
            'user'
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='link-detail')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'link'
        ]
