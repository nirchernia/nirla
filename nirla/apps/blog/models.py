from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	
	created = models.DateTimeField()
	slug = models.SlugField()
	title = models.CharField(max_length=255)
	body = models.TextField()	

		
	def __unicode__(self):
		return self.title
		
	class Meta:	
		verbose_name = "Article"
		verbose_name_plural = "Articles"
		get_latest_by = "created"