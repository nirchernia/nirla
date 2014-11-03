from django.contrib import admin
from nirla.apps.invites.models import Invite, Request_Invite

#This is an invite from an existing user to another non-existing user
class InviteAdmin(admin.ModelAdmin):
	class Meta:
		model = Invite

admin.site.register(Invite, InviteAdmin)





#this is a request for an invite from a non-existing user

def activate_user(modeladmin, reqeust, queryset):
	queryset.user.update(active=True)
	queryset.update(accepted=True)
activate_user.short_description = "Mark User as Active"

class Request_InviteAdmin(admin.ModelAdmin):
	list_display = ['user', 'accepted']
	ordering = ['user']
	actions = [activate_user]
	class Meta:
		model = Request_Invite

admin.site.register(Request_Invite, Request_InviteAdmin)

