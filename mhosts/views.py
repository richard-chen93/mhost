from django.shortcuts import render

from .models import Host_type

def index(request):
    """The home page for Learning Log."""
    return render(request, 'mhosts/index.html')

def host_types(request):
    """Show all host_type."""
    host_types = Host_type.objects.order_by('date_added')
    context = {'host_types': host_types}
    return render(request, 'mhosts/host_types.html', context)

def host_type(request, host_type_id):
    """Show a single host_type, and all its hosts."""
    host_type = Host_type.objects.get(id=host_type_id)
    hosts = host_type.host_set.order_by('-date_added')
    context = {'host_type': host_type, 'hosts': hosts}
    return render(request, 'mhosts/host_type.html', context)