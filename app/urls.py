from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('logout', views.logout)
]