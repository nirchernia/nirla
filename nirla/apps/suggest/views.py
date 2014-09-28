from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from nirla.apps.suggest.forms import suggestionForm
from django.core.urlresolvers import reverse

# Create your views here.

class suggest(View):
	template_name = "suggest/suggest.html"
	
	
	def get(self, request, *args, **kwargs):
		form = suggestionForm()
		
		return render(request, self.template_name, {'form': form})
	
	def post(self, request, *args, **kwargs):
		form = suggestionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('thank_you_page'))
		else:
			form = suggestionForm(request.POST)
			return render(request, self.template_name, {'form': form})

class thankyou(View):
	template_name = "suggest/thank_you.html"
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)