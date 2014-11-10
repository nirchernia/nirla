from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View, TemplateView
from nirla.apps.invites.forms import InviteForm, RequestForm, ActivationForm
from nirla.apps.invites.models import Invite, Request_Invite
from django.contrib.auth.models import User
#from django.core.mail import send_mail
from nirla.apps.invites.utils import send_custom_email
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from nirla.userprofile.models import UserProfile
import uuid
from django.http import HttpResponse



class invite_user(View):
	
	template_name = "invites/invite.html"
	
	
	def get(self, request, *args, **kwargs):
		form = InviteForm()
		return render(request, self.template_name, {'form': form})
		
	
	def post(self, request, *args, **kwargs):
		form = InviteForm(request.POST)
		if form.is_valid():
			#create a random name & password
			random_username = str(uuid.uuid4().hex[:8])
			activation = str(uuid.uuid4().hex)
			
			user = User.objects.create_user(random_username, form.cleaned_data['email'], activation)
			user.is_active = False
			user.save()
			#now create matching UserProfile instance
			new_profile = UserProfile(user=user)
			new_profile.save()
			#now make Invite
			invite = Invite.objects.create(user=user, cookie=uuid.uuid4().hex, token=uuid.uuid4().hex)
			#now set up send_custom_email
			subject = 'Invite Link'
			message = 'Your friend has invited you. \n click on the link: http://www.nir.audio%s \n Your activation code is: %s' % (invite.get_absolute_url(), activation)
			#message ='http://www.nir.audio%s' % invite.get_absolute_url()
			send_custom_email(recipient=user.email, subject=subject, custom_message=message)
			
			return redirect(reverse('home_page'))
		else:
			form = InviteForm()
			return render(request, self.template_name, {'form': form})
			

def confirm_invite(req, token):
	template_name = 'invites/confirm_invite.html'
	
	if req.method == 'POST':
		form = ActivationForm(req.POST)
		
		if form.is_valid():
			invite = get_object_or_404(Invite, token=token)
			user = invite.user
			#auth the user first
			try:
				auth_user = authenticate(username=user.username, password=form.cleaned_data['activation_code'])
			except:
				return HttpResponse('didnt authenticate')
			if auth_user is None:
				return HttpResponse('auth_user is none')
			#mark the user as active
			user.is_active = True
			user.save()
			#log the user in
			login(req, auth_user)
			#change the users name to one desired
			user.username = form.cleaned_data['desired_username']
			user.save()
			#set the password to one desired
			user.set_password(form.cleaned_data['set_password_again'])
			user.save()
			return HttpResponse('activated!')
		else:
			return HttpResponse('form error foo')
	else:
		invite = get_object_or_404(Invite, token=token)
		user = invite.user
		if user.is_active == True:
			return HttpResponse('user is already active')
		else:
			form = ActivationForm()
			return render(req, template_name, {'form': form, 'token': token})


# def confirm_invite_done(req, activation):
# 	template_name = 'invites/confirm_invite.html'
# 	
# 	if req.method == 'POST':
# 		form = ActivationForm(req.POST)
# 		if form.is_valid():
# 			invite = get_object_or_404(Invite, token=token)
# 			user = invite.user
# 			if user.is_active == True:
# 				return HttpResponse('user is already active')
# 				#return redirect(reverse('home_page'))
# 			user.is_active == True
# 			user.save()
# 			try:
# 				auth_user = authenticate(username=user.username, password=form[activation_code])
# 			except:
# 				return HttpResponse('didnt authenticate')
# 			if auth_user is None:
# 				return HttpResponse('auth_user is none')
# 				#return redirect(reverse('home_page'))
# 			login(req, auth_user)
# 			return HttpResponse('you activated your account')
# 		else:
# 			return HttpResponse('form error foo')
# 	else:
# 		form = ActivationForm()
# 		return render(req, template_name, {'form': form})

	
	
# 	invite = get_object_or_404(Invite, token=token)
# 	user = invite.user
# 	if user.is_active == True:
# 		return HttpResponse('user is already active')
# 		#return redirect(reverse('home_page'))
# 	user.is_active == True
# 	user.save()
# 	try:
# 		auth_user = authenticate(username=user.username, password=activation)
# 	except:
# 		return HttpResponse('didnt authenticate')
# 	if auth_user is None:
# 		return HttpResponse('auth_user is none')
# 		#return redirect(reverse('home_page'))
# 	login(req, auth_user)
# 	return redirect(reverse('password_change_done'))

	

def login_user(req):
  if req.user.is_authenticated():
    return redirect(reverse('home_page'))
  if 'token' in req.COOKIES:
    try:
      invite = Invite.objects.get(cookie=req.COOKIES['token'])
    except Invite.DoesNotExist:
	  resp = redirect(reverse('home_page'))
	  resp.delete_cookie('token')
	  return resp
    user = authenticate(username=invite.user.username, password='**')
    if user is None:
      return redirect(reverse('home_page'))
    login(req, user)
  return redirect(reverse('home_page'))		
  
  

class request_invite(View):
	
	template_name = "invites/request_invite.html"
	
	def get(self, request, *args, **kwargs):
		form = RequestForm()
		return render(request, self.template_name, {'form': form})
		
	
	def post(self, request, *args, **kwargs):
		form = RequestForm(request.POST)

		
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['create_password_again'])
			user.first_name=form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.is_active = False
			user.save()
			#now create matching UserProfile instance
			new_profile = UserProfile(user=user)
			new_profile.save()
			#need to make instance of request-invite
			req_invite = Request_Invite.objects.create(user=user, accepted=False)
			#send them an email
			subject= "We have received your request"
			message= "Thank you for your interest in www.nir.audio, we will notify you when we have room for additional users."
			send_custom_email(recipient=user.email, subject=subject, custom_message=message)
			#send them to thank you page
			return redirect(reverse('request_thank_you_page'))
		else:
			form = RequestForm(request.POST)
			return render(request, self.template_name, {'form': form})



class thank_you(TemplateView):
	
	template_name = "invites/thank_you.html"
	
		