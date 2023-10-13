from django import forms
from .models import Ip
from django.forms import ModelForm


class IpForm(ModelForm):
    class Meta:
        model = Ip
        fields = ['fio', 'cabinet', 'department', 'user_name', 'pc_name', 'ip']
