"""Defines url patterns for mhosts."""

from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
        # Show all groups.
    url(r'^groups/$', views.groups, name='groups'),
    
    # Detail page for a single group.
    url(r'^groups/(?P<group_id>\d+)/$', views.group, name='group'),

        # Page for adding a new group.
    url(r'^new_group/$', views.new_group, name='new_group'),

        # Page for editing an group.
    url(r'^edit_group/(?P<group_id>\d+)/$', views.edit_group, name='edit_group'),

        # Page for deleting an group.
    url(r'^delete_group/(?P<group_id>\d+)/$', views.delete_group, name='delete_group'),
    
    #Page for adding a new host.
    url(r'^new_host/(?P<group_id>\d+)/$', views.new_host, name='new_host'),
    
    # Page for editing an host.
    url(r'^edit_host/(?P<host_id>\d+)/$', views.edit_host, name='edit_host'),

    # Page for deleting an host.
    url(r'^delete_host/(?P<host_id>\d+)/$', views.delete_host, name='delete_host'),

    #connect to your host
    url(r'^categoria/([0-9]+)/$', views.connect, name='connect'),

        #configure IE browser
    url(r'ieconfig/$', views.ieconfig, name='ieconfig'),
]

