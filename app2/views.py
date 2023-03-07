from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def second_app2(request):
    return HttpResponse('<h3>This is second app views 1</h3>')

def third_app2(request):
    return HttpResponse('<h1>This is second app views 2</h1>')
