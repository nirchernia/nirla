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
		return (reverse('invite', args=[self.token]))
	