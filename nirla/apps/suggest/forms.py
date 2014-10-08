from django.forms import ModelForm
from nirla.apps.suggest.models import *
from django import forms


class suggestionForm(ModelForm):
	
	class Meta:
		model = Suggestion
        fields = (
            'name',
            'link',
            'email',
            'message',           
            
        )
        
       
