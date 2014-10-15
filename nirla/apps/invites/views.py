from django.shortcuts import render
from django.views.generic.base import View
#need to import InviteForm

class invite_user(View):
	
	template_name = #need template.html here	
	
	def get(self, request, *args, **kwargs):
		form = InviteForm()
		return render(request, self.template_name, {'form': form})
		
	
	def post(self, request, *args, **kwargs):
		if.form.is_valid()
		user = User.objects.create_user(form.cleaned_data['first_name'], form.cleaned_data['email'], '**')
		user.first_name=form.cleaned_data['first_name']
		user.last_name = form.cleaned_data['last_name']
		user.is_active = False
		user.save()
		#now make invite
		invite = Invite.objects.create(user=user, cookie='ck-test', token='tk-test')
		send_mail('Subject', 'Link: http://nir.audio%s' % invite.get_absolute_url(), [user.email])
		return redirect(reverse('home_page')
		

def confirm_invite(req, token):
	invite = get_object_or_404(Invite, token=token)
	user = invite.user
	if user.is_active == True:
		return redirect(reverse('home_page'))
	login(req, auth_user)
	return redirect(reverse('home_page'))
	
# need login user view	
	
		