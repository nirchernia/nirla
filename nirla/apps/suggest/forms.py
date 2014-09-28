from django.forms import ModelForm
from nirla.apps.suggest.models import *


class suggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        fields = (
            'name',
            'link',
            'email',
            'message',
            
        )
        
       
