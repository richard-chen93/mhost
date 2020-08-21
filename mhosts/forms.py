from django import forms

from .models import Group, Host

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['text']
        labels = {'text': ''}

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}