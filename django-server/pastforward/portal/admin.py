from django.contrib import admin

# Register your models here.

from .models import Team, CurrentRound

admin.site.register(Team)
admin.site.register(CurrentRound)
