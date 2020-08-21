"""Defines url patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
        # Show all groups.
    url(r'^groups/$', views.groups, name='groups'),
    
    # Detail page for a single group.
    url(r'^groups/(?P<group_id>\d+)/$', views.group, name='group'),

    #     # Page for adding a new group.
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    # # Page for adding a new entry.
    # url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    
    # # Page for editing an entry.
    # url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    #     name='edit_entry'),
]