from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from nirla.apps.invites.forms import InviteForm
from nirla.apps.invites.models import Invite
from django.contrib.auth.models import User
#from django.core.mail import send_mail
from nirla.apps.invites.utils import send_custom_email
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

class invite_user(View):
	
	template_name = "invites/invite.html"
	
	
	def get(self, request, *args, **kwargs):
		form = InviteForm()
		return render(request, self.template_name, {'form': form})
		
	
	def post(self, request, *args, **kwargs):
		form = InviteForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['first_name'], form.cleaned_data['email'], '**')
			user.first_name=form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.is_active = False
			user.save()
			#now make Invite
			invite = Invite.objects.create(user=user, cookie='ck-test', token='tk-test')
			#now set up send_custom_email
			message ='www.nir.audio%s' % invite.get_absolute_url()
			send_custom_email(recipient=user.email, custom_message=message)
			return redirect(reverse('home_page'))
		else:
			form = InviteForm()
			return render(request, self.template_name, {'form': form})
			

def confirm_invite(req, token):
	invite = get_object_or_404(Invite, token=token)
	user = invite.user
	if user.is_active == True:
		return redirect(reverse('home_page'))
	user.is_active == True
	user.save()
	auth_user = authenticate(username=user.username, password='**')
	if auth_user is None:
		return redirect(reverse('home_page'))
	login(req, auth_user)
	return redirect(reverse('home_page'))

	

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