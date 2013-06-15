from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hitupp.views.home', name='home'),
    # url(r'^hitupp/', include('hitupp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('backend.account',
    url('^login$', 'process_login'),
    url('^logout$', 'process_logout'),
    url('^signin$', 'signin_page', name="signin"),
)

urlpatterns += patterns('backend.storyboard',
    url('^storyboard$', 'storyboard'),
)

urlpatterns += patterns('backend.experience',
    url('^experience$', 'experience'),
)

urlpatterns += patterns('backend.home',
    url('^home$', 'home_page', name="home"),
)

urlpatterns += patterns('backend.views',
    url('^$', 'front_page'),
)

urlpatterns += patterns('backend.register',
    url('^signup$', 'signup_page', name="signup"),
    url('^register$', 'process_registration'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )


