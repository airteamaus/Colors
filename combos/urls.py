from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('combos.views',
    url(r'^$', 'latest_combos',  name='latest_combos'),
    url(r'^list$', 'list_combos',  name='list_combos'),
    url(r'^(?P<slug>[0-9A-Za-z\-_]+)$', 'show_combo', name='show_combo')
)