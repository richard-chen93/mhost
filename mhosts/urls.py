"""Defines url patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
        # Show all host_types.
    url(r'^host_types/$', views.host_types, name='host_types'),
    
    # Detail page for a single host_type.
    url(r'^host_types/(?P<host_type_id>\d+)/$', views.host_type, name='host_type'),
]