from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    '''create a homepage'''
    return render(request, 'home.html')
