from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from nirla.apps.blog.views import home, about
from nirla.apps.suggest.views import suggest, thankyou
from django.core.urlresolvers import reverse
#used for serving static locally
from django.conf import settings
#used for serving favicon
from django.views.generic import RedirectView


urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	
	#from blog app
	url(r'^$', home.as_view(), name="home_page"),
	url(r'^about/$', about.as_view(), name='about_page'),
	
	#from suggest app
	url(r'^suggest/$', suggest.as_view(), name='suggest_page'),
	url(r'^thankyou/$', thankyou.as_view(), name='thank_you_page'),
	
	#serving static on local
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	
	#serving favicon
	#(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
	
)