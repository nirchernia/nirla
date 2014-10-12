from django.contrib import admin
from nirla.userprofile.models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	list_display_links = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)