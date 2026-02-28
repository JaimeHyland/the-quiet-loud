from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def today(request):
    return render(request, 'today.html')

def journey(request):
    return render(request, 'journey.html')

def support(request):
    return render(request, 'support.html')