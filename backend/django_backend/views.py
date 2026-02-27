from django.http import HttpResponse


def home(request):
    return HttpResponse(
        '<h1>🚀 Django is up and running!</h1>'
        '<p>Use /accounts/ for login/signup.</p>'
    )
