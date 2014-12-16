from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from nirla.apps.blog.views import home, about, article_view
from nirla.apps.suggest.views import suggest, thankyou
from django.core.urlresolvers import reverse
from nirla.userprofile.views import Login, Logout, Signup
from nirla.apps.invites.views import invite_user, confirm_invite, request_invite, thank_you
#used for serving static locally
from django.conf import settings
from django.contrib.auth.decorators import login_required #decorator wanabe for CBVs
from django.contrib.auth.views import password_change



urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	
	#blog app
	url(r'^$', home.as_view(), name="home_page"),
	url(r'^about/$', about.as_view(), name='about_page'),
	url(r'^article/(?P<title>(.*))$', article_view.as_view(), name="article_view"),
	
	#suggest app
	url(r'^suggest/$', suggest.as_view(), name='suggest_page'),
	url(r'^thankyou/$', thankyou.as_view(), name='thank_you_page'),
	
	#userprofile
	url(r'^login/$', Login.as_view(), name='login_page'),
	url(r'^logout/$', Logout.as_view(), name='logout_page'),
	#url(r'^signup/$', Signup.as_view(), name='signup_page'), #commented out because this is invite only app
	
	#invite app
	url(r'^invite-member/$', login_required(invite_user.as_view()), name="invite_user_page"), #for memebers to invite new members
	url(r'^confirm-invite/(?P<token>[\w-]+)/$', confirm_invite, name="confirm_invite_page"),
	url(r'^request-invite/$', request_invite.as_view(), name="request_invite_page"), #for non-registered members to use
	url(r'^thank-you/$', thank_you.as_view(), name='request_thank_you_page'), #after request invite
	url(r'^set-password/$', password_change, name='password_change_done'),
	
	
	
	#serving static on local
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	
	
)

