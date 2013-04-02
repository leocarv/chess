from django.conf.urls import *

urlpatterns += patterns('',
    url(r'login', 'game.views.do_login'),
    url(r'logout', 'game.views.do_logout')
)
