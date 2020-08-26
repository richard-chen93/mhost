from django import forms

from .models import Group, Host

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['text','os_type']
        labels = {'text': 'group name'}

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['text', 'host_name', 'host_ip']
        labels = {'text': 'description'}
        widgets = {'text': forms.Textarea(attrs={'cols': 20})}
