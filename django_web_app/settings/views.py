from django.shortcuts import render, redirect
from .forms import SettingForm

def index(request):
    form = SettingForm()
    return render(request, 'settings/index.html', {form : form})