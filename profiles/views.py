from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    """View function for home page of site."""
    context = {}
    return render(request, 'index.html', context=context)


@login_required
def profile(request):
    context = {}
    return render(request, 'profile.html', context=context)
