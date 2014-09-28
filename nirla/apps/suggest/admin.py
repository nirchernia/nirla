from django.contrib import admin
from nirla.apps.suggest.models import Suggestion

# Register your models here.

class SuggestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Suggestion


admin.site.register(Suggestion, SuggestionAdmin)


