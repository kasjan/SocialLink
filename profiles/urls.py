from django.urls import path
from . import views

urlpatterns = [
    path('socials/', views.SocialList.as_view(), name='social-list'),
    path('socials/<int:pk>', views.SocialDetail.as_view(),
         name='social-detail'),
    path('link/', views.LinkList.as_view(), name='link-list'),
    path('link/<int:pk>', views.LinkDetail.as_view(), name='link-detail'),
    path('users/', views.UserLink.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('', views.ApiRoot.as_view(), name='api-root')
]
