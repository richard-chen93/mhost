from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from .models import Group,Host
from .forms import GroupForm,HostForm

from django.contrib.auth.decorators import login_required


def index(request):
    """The home page for mhost."""
    return render(request, 'mhosts/index.html')

@login_required
def groups(request):
    """Show all group."""
    groups = Group.objects.filter(owner=request.user).order_by('date_added')
    context = {'groups': groups}
    return render(request, 'mhosts/groups.html', context)

@login_required
def group(request, group_id):
    """Show a single group, and all its hosts."""
    group = Group.objects.get(id=group_id)
    #确认请求的主题属于当前用户
    if group.owner != request.user:
        raise Http404
    hosts = group.host_set.order_by('-date_added')
    context = {'group': group, 'hosts': hosts}
    return render(request, 'mhosts/group.html', context)


def new_group(request):
    """Add a new group."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GroupForm()
    else:
        # POST data submitted; process data.
        form = GroupForm(request.POST)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.owner = request.user
            new_group.save()
            return HttpResponseRedirect(reverse('mhosts:groups'))

    context = {'form': form}
    return render(request, 'mhosts/new_group.html', context)

@login_required
def new_host(request, group_id):
    """Add a new host for a particular group."""
    group = Group.objects.get(id=group_id)
    if group.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = HostForm()

    else:
        # POST data submitted; process data.
        form = HostForm(data=request.POST)

        
        if form.is_valid():
            new_host = form.save(commit=False)
            new_host.group = group
            new_host.save()

            return HttpResponseRedirect(reverse('mhosts:group',
                                                args=[group_id]))

    context = {'group': group, 'form': form}
    return render(request, 'mhosts/new_host.html', context)

@login_required
def edit_host(request, host_id):
    """Edit an existing host."""
    host = Host.objects.get(id=host_id)
    group = host.group
    if group.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current host.
        form = HostForm(instance=host)
    else:
        # POST data submitted; process data.
        form = HostForm(instance=host, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mhosts:group',
                                        args=[group.id]))
    
    context = {'host': host, 'group': group, 'form': form}
    return render(request, 'mhosts/edit_host.html', context)