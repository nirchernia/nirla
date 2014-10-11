from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

class Login(View):
	template_name = "auth/login.html"
		
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			#render the login template
			return render(request, self.template_name)
		else:
			#redirect to home_page
			return redirect(reverse('home_page'))
		
	def post(self, request, *args, **kwargs):
		username = request.POST.get('username', '') # the '' is the default value
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			#now redirect to success page
			return redirect(reverse('home_page'))
		else:
			#show an error page
			return redirect(reverse('login_page'))
			
		
class Logout(View):
	
	def get(self, request, *args, **kwargs):
		logout(request, user)
		return redirect(reverse('home_page'))
	
	
	
class Signup(View):
	template_name = "auth/signup.html"
	form = UserCreationForm()
	
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return render(request, self.template_name, {'form': self.form})
	
	
	def post(self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid(): #correct this
			new_user = form.save()
			#now create a UserProfile instance and save it
			new_UserProfile = UserProfile(user=new_user)
			new_UserProfile.save()
			#now log the user in
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, new_user)
			return redirect(reverse('home_page'))
		else:
			#failuire for some reason
			form = UserCreationForm()
			return render(request, self.template_name, {'form':form})
		
		
		

	      