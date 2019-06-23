from django.contrib import admin
from .models import Player
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('user', 'current_level')

admin.site.register(Player, PlayerAdmin)
