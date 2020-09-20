import subprocess
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from .models import Group, Host
from .forms import GroupForm, HostForm
# from .forms import SearchForm

from django.db.models import Q

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """The home page for mhost."""
    """Show all groups, and os_type"""
    groups = Group.objects.filter(owner=request.user).order_by('id')
    context = {'groups': groups}
    return render(request, 'mhosts/groups.html', context)



@login_required
def groups(request):
    """Show all groups, and os_type"""
    groups = Group.objects.filter(owner=request.user).order_by('id')

    ##
    # o = []
    # grp = Group.objects.filter(owner=request.user).order_by('date_added').values()
    # for i in grp:
    #     o.append(i['os_type'])

    ##
    context = {'groups': groups}
    # context = {'groups': groups, 'o': o}
    return render(request, 'mhosts/groups.html', context)


@login_required
def group(request, group_id):
    """Show a single group, and all its hosts."""

    group = Group.objects.get(id=group_id)
    """find group and host query set in database"""
    # 确认请求的主题属于当前用户
    if group.owner != request.user:
        raise Http404
    hosts = group.host_set.order_by('host_ip')
    #.count函数可以查询查询集的数量
    #定义1-300的列表传递给render函数
    # seq = {}
    # seq['c'] = list(range(1,6))

    context = {
        'group': group, 'hosts': hosts, 
    }

    if group.os_type == 'windows':
        return render(request, 'mhosts/win_group.html', context)
    else:
        return render(request, 'mhosts/linux_group.html', context)
    # return render(request, 'mhosts/group.html', context)


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


#新增编辑组
@login_required
def edit_group(request, group_id):
    """Edit an existing group."""
    group = Group.objects.get(id=group_id)
    if group.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current group.
        form = GroupForm(instance=group)
    else:
        # POST data submitted; process data.
        form = GroupForm(instance=group, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mhosts:groups'))

    context = {'group': group, 'form': form}
    return render(request, 'mhosts/edit_group.html', context)


@login_required
def delete_group(request, group_id):
    """delete an existing group."""
    group = Group.objects.get(id=group_id)
    if group.owner != request.user:
        raise Http404

    group.delete()
    return HttpResponseRedirect(reverse('mhosts:groups'))


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
def search_host(request, group_id):
    """search a new host in a particular group."""
    group = Group.objects.get(id=group_id)
    if group.owner != request.user:
        raise Http404

    q = request.GET.get('q')

    qs = Host.objects.filter(group_id=group_id)
    hosts = qs.filter(Q(host_ip__icontains=q)|Q(host_name__icontains=q))

    context = {'group': group, 'hosts': hosts}
    if group.os_type == 'windows':
        return render(request, 'mhosts/win_group.html', context)
    else:
        return render(request, 'mhosts/linux_group.html', context)



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


@login_required
def delete_host(request, host_id):
    """delete an existing host."""
    host = Host.objects.get(id=host_id)
    group = host.group
    if group.owner != request.user:
        raise Http404

    host.delete()
    return HttpResponseRedirect(reverse('mhosts:group',args=[group.id]))

#帮助文件 配置IE浏览器
def ieconfig(request):
    return render(request, 'mhosts/ieconfig.html')



