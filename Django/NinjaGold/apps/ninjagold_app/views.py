from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *
import random

def generate_random(start,end):
    return random.randrange(start,end)

def index(request):
    return render(request,'ninjagold_app/index.html')

def process(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    else:
        timestamp = datetime.now()
        if request.POST['building'] == 'farm':
            gold = generate_random(10,20)
            request.session['gold'] += gold
            request.session['activities'].append(['earn', 'Earned %d from the farm! ( %s )' % (gold, timestamp)])
        elif request.POST['building'] == 'cave':
            gold = generate_random(5,10)
            request.session['gold'] += gold
            request.session['activities'].append(['earn', 'Earned %d from the cave! ( %s )' % (gold, timestamp)])
        elif request.POST['building'] == 'house':
            gold = generate_random(5,10)
            request.session['gold'] += gold
            request.session['activities'].append(['earn', 'Earned %d from the house! ( %s )' % (gold, timestamp)])
        elif request.POST['building'] == 'casino':
            earn_loss = generate_random(0,1)
            if earn_loss == 1:
                result = 'earn'
            else:
                result ='loss'
            gold = generate_random(0,50)
            if result == 'loss':
                request.session['gold'] -= gold
                request.session['activities'].append(['loss', 'Entered a casino and lost %d golds... Ouch... ( %s )' % (gold, timestamp)])
            else:
                request.session['gold'] += gold
                request.session['activities'].append(['earn', 'Earned %d golds from the casino!( %s )' % (gold, timestamp)])
    return redirect ('/')
def reset(request):
    request.session.clear()
    return redirect('/') 
