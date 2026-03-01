from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')


@login_required
def today(request):
    return render(request, 'today.html')


@login_required
def journey(request):
    return render(request, 'journey.html')


def support(request):
    return render(request, 'support.html')
