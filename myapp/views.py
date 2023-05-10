from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h1>About</h1><a href="http://127.0.0.1:8000/">Go to Home</a>')

# def result(request):
#     user_input_age = int(request.GET["age"])
#     prediction = fake_model.fake_predict(user_input_age)
#     return render(request, 'result.html', {'prediction':prediction})