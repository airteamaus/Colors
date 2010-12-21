from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('users.views',
    url(r'^request$', 'request_account',  name='request_account'),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^received$', 'direct_to_template', {'template': 'users/please_check_email.html'}, name='please_check_your_email'),
)
    
