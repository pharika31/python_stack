from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *
# Create your views here.
def index(request):

    context ={
    'random_string' : get_random_string(length=12, allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    }
    if 'attempt' not in request.session:
        request.session['attempt']=1
    else:
        request.session['attempt'] +=1

    return render(request,'random_app/index.html', context)

def random(request):
    return redirect('/')
def reset(request):
    request.session.clear()
    return redirect('/')
