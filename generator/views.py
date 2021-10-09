from typing import Generator
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    # return HttpResponse('Hello ! Welcome to Django')
    return render(request, 'generator/home.html',{'password':'123409'})

def eggs(request):
    return HttpResponse('<h1>Eggs are sold<h1>')


def password(request):

    # pwd='testing'

    characters=list('abcdefghijklmnopqrstuvwxyz')
    #length=10
    length=int(request.GET.get('S'))

    if request.GET.get('Uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        characters.extend('0123456789')
    
    if request.GET.get('special'):
        characters.extend('~!@#$%^&*(){[}]/-,.')
    pwd=''

    for x in range(length):
        pwd += random.choice(characters)

    return render(request, 'generator/password.html',{'password' : pwd})



def about(request):
    # return HttpResponse('Hello ! Welcome to Django')
    return render(request, 'generator/about.html')