"""Urls.py file."""
# Django
from django.urls import path

# Local
from . import views

urlpatterns = [
    path('<str:username>', views.ProfileView.as_view()),

    # DJANGO REST FRAMEWORK URLS
    path('api/socials/', views.SocialList.as_view(), name='social-list'),
    path('api/socials/<int:pk>', views.SocialDetail.as_view(),
         name='social-detail'),
    path('api/link/', views.LinkList.as_view(), name='link-list'),
    path('api/link/<int:pk>', views.LinkDetail.as_view(), name='link-detail'),
    path('api/users/', views.UserLink.as_view(), name='user-list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('api/', views.ApiRoot.as_view(), name='api-root'),

]
