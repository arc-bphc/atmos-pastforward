from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
<<<<<<< HEAD
    path('leaderboard/', views.leaderboard, name='leaderboard'),
=======
>>>>>>> f70f5c50f710cef184e7c730c6a7d216d58af9e9
    path('registration/', views.registration, name='registration'),
]
