from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Estou na web!')

def segundo(request):
    return HttpResponse('<h1>Segudno</h1>')