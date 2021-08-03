from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('',  first_page, name='first-page'),

    path('home_view', home, name='home_view'),

    path('add_tweet/',  PostCreateView.as_view(), name='add_tweet'),

    path('tweet/<int:pk>/', post_view, name='post_view'),

    path('comment/add/<id>', add_comment, name='add_comment'),

    path('user/<user>/', user_view, name='user_view'),

    path('settings/', settings_view, name="settings"),

    path('follow/<int:followed>/<int:follower>/', follow, name="follow"),
    path('search/', search, name="search"),

    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),

    path('post/<int:pk>/preference/<int:userpreference>', postpreference, name='postpreference'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
