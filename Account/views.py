from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return HttpResponse ("<h1> Omniat </h1>")

def profile(request):
    return HttpResponse