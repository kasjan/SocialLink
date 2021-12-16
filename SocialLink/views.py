from django.contrib.auth.models import User
from django.shortcuts import render
from profiles.models import Link


def profile_view(request, username):

    queryset = Link.objects.filter(user__username__exact=username)

    context = {
        "object_list": queryset,
        "username": username
    }

    return render(request, "user.html", context)
