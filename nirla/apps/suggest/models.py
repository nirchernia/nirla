from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.


class Suggestion(models.Model):
	
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	name = models.CharField(max_length=225, blank=False)
	link = models.URLField(max_length=800, blank=True)
	email = models.EmailField(max_length=300, blank=True)
	message = models.TextField(max_length=600, blank=True)
	
	def __unicode__(self):
		return smart_unicode(self.name)
	
	class Meta:
		verbose_name = "Suggestion"
		verbose_name_plural = "Suggestions"
		