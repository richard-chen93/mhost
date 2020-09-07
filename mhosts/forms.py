from django import forms

from .models import Group, Host

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['text', 'os_type']
        labels = {'text': 'group name'}

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['host_name', 'host_ip', 'user_name', 'user_pass', 'text']
        labels = {'text': 'description'}
        widgets = {'text': forms.Textarea(attrs={'cols': 30})}
        # widgets = {'user_pass': forms.PasswordInput()}
