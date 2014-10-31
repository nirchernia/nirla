from django import forms
from nirla.apps.invites.models import Invite

class InviteForm(forms.Form):
  username = forms.CharField(max_length=20)
  first_name = forms.CharField(max_length=40)
  last_name = forms.CharField(max_length=40)
  email = forms.EmailField()
 

class RequestForm(forms.Form):
	username = forms.CharField(max_length=20)
	first_name = forms.CharField(max_length=40)
	last_name = forms.CharField(max_length=40)
	email = forms.EmailField()