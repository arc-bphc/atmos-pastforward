from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('registration/', views.registration, name='registration'),
    path('gameplay/<slug:team_name>/', views.gameplay, name="gameplay"),
    path('gameplay/<slug:team_name>/<int:phase>/', views.gameplay, name="gameplay"),
]
