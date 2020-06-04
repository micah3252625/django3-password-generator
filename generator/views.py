from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special-chars'):
        characters.extend(list(string.punctuation))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length_password = int(request.GET.get('length'))

    thePassword = ""

    for x in range(length_password):
        thePassword += random.choice(characters)

    return render(request, 'generator/home.html',  {'password': thePassword})

