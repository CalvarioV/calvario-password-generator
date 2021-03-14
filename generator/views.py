from django.shortcuts import render
#from django.conf import settings
import random
from django.http import HttpResponse
# Create your views here.


#def home(request):
   # return HttpResponse('This is the OG homepage.')


def home(request):
    return render(request, 'generator/formhome.html')


def about(request):
    return render(request, 'generator/audio.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 8))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

