from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('registration/', views.registration, name='registration'),
]
