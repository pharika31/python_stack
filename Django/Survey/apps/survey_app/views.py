from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *
# Create your views here.
def index(request):
    return render(request,'survey_app/index.html')
def process(request):
    print "Entered process method"
    request.session['name'] = request.POST['name']
    request.session['loc'] = request.POST['loc']
    request.session['lang']=request.POST['lang']
    request.session['comment']= request.POST['comment']
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] = 1

    return redirect('/result')

def result(request):
    print "entered Result method"
    return render(request,'survey_app/result.html')
