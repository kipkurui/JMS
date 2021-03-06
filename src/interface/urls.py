from django.conf.urls import patterns, url, include
from interface import views

urlpatterns = patterns('interface.views',
	url(r'^account/login/?', 'sign_in'),	
	url(r'^account/logout/?', 'sign_out'),	
	url(r'^workflows/visualize', 'workflow_visualizer'),	
	url(r'^workflows', 'workflows'),
	url(r'^tools', 'tools'),
	url(r'^jobs/?', 'jobs'),
	url(r'^settings/?', 'settings'),
	url(r'^', 'index'),	
)
