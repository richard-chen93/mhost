from django.shortcuts import render

from .models import Group


def index(request):
    """The home page for Learning Log."""
    return render(request, 'mhosts/index.html')


def groups(request):
    """Show all group."""
    groups = Group.objects.order_by('date_added')
    context = {'groups': groups}
    return render(request, 'mhosts/groups.html', context)


def group(request, group_id):
    """Show a single group, and all its hosts."""
    group = Group.objects.get(id=group_id)
    hosts = group.host_set.order_by('-date_added')
    context = {'group': group, 'hosts': hosts}
    return render(request, 'mhosts/group.html', context)
