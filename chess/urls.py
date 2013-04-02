from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^access/', include('access.urls')),
    url(r'^$', 'access.views.show_system'),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^coverage/', redirect_to,
            {'url': settings.STATIC_URL + 'coverage/index.html'}),
    )
