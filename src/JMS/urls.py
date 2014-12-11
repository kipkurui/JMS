from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^api/jms/', include('job.urls')),
	url(r'^api/users/', include('users.urls')),
    #url(r'^docs/?', include('rest_framework_swagger.urls')),
    url(r'^admin/?', include(admin.site.urls)),
	url(r'^', include('interface.urls')),
)