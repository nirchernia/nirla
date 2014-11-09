from django import forms


class InviteForm(forms.Form):
  username = forms.CharField(max_length=20)
  first_name = forms.CharField(max_length=40)
  last_name = forms.CharField(max_length=40)
  email = forms.EmailField()
 

class RequestForm(forms.Form):
	username = forms.CharField(max_length=20)
	create_password = forms.CharField(widget=forms.PasswordInput(render_value = True))
	create_password_again = forms.CharField(widget=forms.PasswordInput(render_value = True))
	first_name = forms.CharField(max_length=40)
	last_name = forms.CharField(max_length=40)
	email = forms.EmailField()
	
class ActivationForm(forms.Form):
	activation_code = forms.CharField(max_length=33)
	set_password = forms.CharField(widget=forms.PasswordInput(render_value = True))
	set_password_again = forms.CharField(widget=forms.PasswordInput(render_value = True))
	
	