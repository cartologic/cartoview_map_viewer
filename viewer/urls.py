from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns('',
   url(r'^maps/$', views.list_maps, name='viewer.list_maps'),
   url(r'^maps/(?P<map_id>\d+)/view/$', views.view_map, name='viewer.view_map'),

   url(r'^maps/(?P<map_id>\d+)/embed/$', views.embed_map, name='viewer.embed_map'),
   url(r'^maps/(?P<map_id>\d+)/config.json', views.map_config, name='viewer.map_config'),
   # apps urls
   url(r'^new/$', views.new, name='viewer.new'),
   url(r'^(?P<instance_id>\d+)/edit/$', views.edit, name='viewer.edit'),
   url(r'^(?P<instance_id>\d+)/view/$', views.view_app , name='viewer.view')
)
