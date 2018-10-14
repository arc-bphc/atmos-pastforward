from django.contrib import admin

# Register your models here.

from .models import Team, Contest

admin.site.register(Team)
admin.site.register(Contest)
