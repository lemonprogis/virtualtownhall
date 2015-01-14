from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^polls/$', 'poll.views.view_polls'),
    url(r'^answer/$', 'poll.views.post_answer'),
)
