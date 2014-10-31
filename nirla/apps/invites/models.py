from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Invite(models.Model):
	user = models.OneToOneField(User)
	cookie = models.SlugField()
	token = models.SlugField()
	
	def __unicode__(self):
		return u"%s's invite" % (self.user)
		
	def get_absolute_url(self):
		return reverse('confirm_invite_page', args=[self.token])

class Request_Invite(models.Model):
	user = models.OneToOneField(User)
	acceptance = models.BooleanField(default=False)
	
	def __unicode__(self):
		return u"%s's request" % (self.user)
		
	def accept_request(self):
		pass
		#need to change boolean to True
		#need to change User to active
		