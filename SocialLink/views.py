from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from profiles.models import Link


def profile_view(request, username):

    user = User.objects.get(username=username)
    queryset = Link.objects.filter(user__username__exact=username)

    context = {
        "object_list": queryset,
        "user": user
    }

    return render(request, "user.html", context)
