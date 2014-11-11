from django import forms


class InviteForm(forms.Form):
	email = forms.EmailField()
 

class RequestForm(forms.Form):
	username = forms.CharField(max_length=20)
	create_password = forms.CharField(widget=forms.PasswordInput(render_value = True))
	create_password_again = forms.CharField(widget=forms.PasswordInput(render_value = True))
	first_name = forms.CharField(max_length=40)
	last_name = forms.CharField(max_length=40)
	email = forms.EmailField()
	
	def clean(self): #clean is a built in method, this is overridding it.
		create_password = self.cleaned_data.get('create_password')
		create_password_again = self.cleaned_data.get('create_password_again')
		
		if create_password and create_password != create_password_again:
			raise forms.ValidationError("Passwords don't match")
		return self.cleaned_data
	
class ActivationForm(forms.Form):
	activation_code = forms.CharField(max_length=33)
	desired_username = forms.CharField(max_length=20)
	set_password = forms.CharField(widget=forms.PasswordInput(render_value = True))
	set_password_again = forms.CharField(widget=forms.PasswordInput(render_value = True))
	
	
	def clean(self): #clean is a built in method, this is overridding it.
		set_password = self.cleaned_data.get('set_password')
		set_password_again = self.cleaned_data.get('set_password_again')
		username = self.cleaned_data.get('desired_username')
		
		if set_password and set_password != set_password_again:
			raise forms.ValidationError("Passwords don't match")
			
		if User.objects.filter(username=username).exists():
			raise ValidationError('Username already taken.')
		
		return self.cleaned_data
	
	