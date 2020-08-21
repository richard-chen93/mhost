"""Defines url patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
        # Show all topics.
    url(r'^host_types/$', views.host_types, name='host_types'),
    
]