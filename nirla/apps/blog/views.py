from nirla.apps.blog.models import Article
from django.views.generic.base import TemplateView, View
from django.shortcuts import render
import markdown
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse


# Create your views here.

class home(View):
	""" The main page of the blog. This view include pagination """ 
	template_name = "blog/index.html"
	
 	def get(self, request, *args, **kwargs):
 		
 		main_article = Article.objects.latest()
 		prev_articles = Article.objects.all().order_by('-created')[1:]
 		paginator = Paginator(prev_articles, 4)
 		
 		page = request.GET.get('page')
 		try:
 			pa= paginator.page(page)
 		except PageNotAnInteger:
 			pa = paginator.page(1)
 		except EmptyPage:
 			pa = paginator.page(paginator.num_pages)
 		
		return render(request, self.template_name, {'main_article': main_article, 'prev_articles': pa})


class about(View):
	""" The about page of the blog. """ 
	template_name = "blog/about.html"
	
 	def get(self, request, *args, **kwargs):
 		
		return render(request, self.template_name)

    
    
   
