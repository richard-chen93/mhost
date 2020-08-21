from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Group
from .forms import GroupForm


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


def new_host(request, group_id):
    """Add a new host for a particular group."""
    group = Topic.objects.get(id=group_id)
    if group.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_host = form.save(commit=False)
            new_host.group = group
            new_host.save()
            return HttpResponseRedirect(reverse('mhosts:group',
                                                args=[group_id]))

    context = {'group': group, 'form': form}
    return render(request, 'mhosts/new_host.html', context)
