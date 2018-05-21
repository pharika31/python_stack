from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *
# Create your views here.
def index(request):
    return render(request,'session_words/index.html')

def addWords(request):
    if request.method== 'POST':
        time = strftime('%#H:%M:%S%p, %B %#d %Y', localtime())
        if 'words' not in request.session:
            request.session['words']=[]
        if 'big' in request.POST:
            data = {
            'word' : request.POST['word'],
            'color':request.POST['color'],
            'font': 'large',
            'time': time
            }

        else:
            data ={
            'word' : request.POST['word'],
            'color':request.POST['color'],
            'font': 'normal',
            'time': time
            }
        request.session['words'].append(data)
        request.session.modified = True

    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
