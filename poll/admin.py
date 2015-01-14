from django.contrib import admin
from models import *

class TownHallPollAdmin(admin.ModelAdmin):
	pass

class TownHallResponseAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "answer", "email")

admin.site.register(TownHallPoll, TownHallPollAdmin)
admin.site.register(TownHallResponse, TownHallResponseAdmin)
