from django.db import models
from django.contrib.auth.models import User
from 

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	followers = ManyToManyField('self', symmetrical=False, blank= True, null=True) #double check null and blank
	following = ManyToManyField('self', symmetrical=False, blank=True, null=True)
	likes = ManyToManyField(Article, blank=True, null=True)
	
	def __unicode__(self):
		return u'%s' % self.user.username
	
	class Meta:
		verbose_name = "User Profile"
		verbose_name_plural = "user Profiles"
