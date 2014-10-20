from django.contrib import admin
from nirla.apps.invites.models import Invite




class InviteAdmin(admin.ModelAdmin):
	class Meta:
		model = Invite




admin.site.register(Invite, InviteAdmin)