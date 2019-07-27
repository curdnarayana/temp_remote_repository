from django.contrib import admin
from .models import Profile, Games
# Register your models here.

class AdminProfile(admin.ModelAdmin):
	list_display = ['father_name', 'marks']

class AdminGames(admin.ModelAdmin):
	list_display = ['gno', 'gname']

admin.site.register(Profile, AdminProfile)
admin.site.register(Games, AdminGames)