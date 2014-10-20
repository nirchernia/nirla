from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from nirla.apps.blog.views import home, about
from nirla.apps.suggest.views import suggest, thankyou
from django.core.urlresolvers import reverse
from nirla.userprofile.views import Login, Logout, Signup
from nirla.apps.invites.views import invite_user
#used for serving static locally
from django.conf import settings



urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	
	#blog app
	url(r'^$', home.as_view(), name="home_page"),
	url(r'^about/$', about.as_view(), name='about_page'),
	
	#suggest app
	url(r'^suggest/$', suggest.as_view(), name='suggest_page'),
	url(r'^thankyou/$', thankyou.as_view(), name='thank_you_page'),
	
	#userprofile
	url(r'^login/$', Login.as_view(), name='login_page'),
	url(r'^logout/$', Logout.as_view(), name='logout_page'),
	url(r'^signup/$', Signup.as_view(), name='signup_page'),
	url(r'^request-invite/$', invite_user.as_view(), name="invite_user_page"),
	
	#inviter app
	#url('^invites/', include('inviter.urls', namespace = 'inviter')),
	
	#serving static on local
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	
	
)