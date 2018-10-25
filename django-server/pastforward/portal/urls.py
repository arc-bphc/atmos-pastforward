from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('registration/', views.registration, name='registration'),
    path('round1/<slug:team_name>/', views.round1, name="round1"),
    path('round2/<slug:team_name>/', views.round2, name="round2"),
    path('delete/', views.deleteMonitor, name="deleteMonitor"),
]
