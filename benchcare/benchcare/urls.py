from django.conf.urls import patterns, include, url
from benchcare import views
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^about$', views.about, name = 'about'),
	url(r'^team$', views.team, name = 'team'),
	url(r'^features$', views.features, name = 'features'),
	
	
	url(r'^pricing$', views.pricing_table, name = 'pricingtable'),
	url(r'^howitworks$', views.how_it_works, name = 'howitworks'),
	url(r'^contact$', views.contact_us, name = 'contactus'),
	url(r'^patients/', include('patients.urls')),
	url(r'^appointments/', include('appointments.urls')),
	(r'^accounts/', include('registration.backends.default.urls')),
	
	url(r'^invoice/', include('invoice.urls')),
	url(r'^analytics/', include('analytics.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
