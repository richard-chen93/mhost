from django.contrib import admin

# Register your models here.
from mhosts.models import Host_type,Host
admin.site.register(Host_type)
admin.site.register(Host)
