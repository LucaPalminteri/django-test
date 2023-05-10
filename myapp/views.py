from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Home</h1><a href="http://127.0.0.1:8000/about">Go to About</a>')

def about(request):
    return HttpResponse('<h1>About</h1><a href="http://127.0.0.1:8000/">Go to Home</a>')