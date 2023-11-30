from django import forms
from .models import Setting

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['viettel_key', 'fpt_key', 'rss_key', 'tssfree_key', 'signature']
