from django.contrib import admin
from nirla.apps.invites.models import Invite, Request_Invite
from nirla.apps.invites.utils import send_custom_email

#This is an invite from an existing user to another non-existing user
class InviteAdmin(admin.ModelAdmin):
	class Meta:
		model = Invite

admin.site.register(Invite, InviteAdmin)





#this is a request for an invite from a non-existing user

def activate_user(modeladmin, reqeust, queryset):
	for q in queryset:
		q.user.is_active = True
		q.user.save()
		#send mail telling them that they have been accepted + link to reset their password
		user_email = q.user.email
		subject = "Your request has been accepted!"
		message = "The account for %s has been accepted. You may now log in here: http://www.nir.audio/login/" % q.user.username 
		send_custom_email(recipient=user_email, subject=subject, custom_message=message)
		
	#update every model in the queryset to have accept=True	
	queryset.update(accepted=True)
	
	
	
activate_user.short_description = "Mark User as Active"

class Request_InviteAdmin(admin.ModelAdmin):
	list_display = ['user', 'accepted']
	ordering = ['user']
	actions = [activate_user]
	class Meta:
		model = Request_Invite

admin.site.register(Request_Invite, Request_InviteAdmin)

