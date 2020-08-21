from django.contrib import admin

# Register your models here.
from mhosts.models import Group,Host
admin.site.register(Group)
admin.site.register(Host)
