from django.db import models
from django.contrib.auth.models import User
from nirla.apps.blog.models import Article

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	follower = models.ManyToManyField('self', blank= True, null=True) #symmetrical=False  
	following = models.ManyToManyField('self', blank=True, null=True) #symmetrical=False
	likes = models.ManyToManyField(Article, blank=True, null=True)
	
	def __unicode__(self):
		return u'%s' % self.user.username
	
	class Meta:
		verbose_name = "User Profile"
		verbose_name_plural = "user Profiles"
