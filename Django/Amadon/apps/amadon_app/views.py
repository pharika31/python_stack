from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *
# Create your views here.
products = {
'1001': 19.99,
'1002': 24.99,
'1003': 4.99,
'1004': 49.99
}
def index(request):
    return render(request,'amadon_app/index.html')

def buy(request):
    if request.method=='POST':
        if 'quantity' not in request.session:
            request.session['quantity'] = 0
        if 'total_amount' not in request.session:
            request.session['total_amount'] =0
        request.session['price'] = products[request.POST['product_id']] * int(request.POST['quantity'])#price per buy button
        request.session['quantity'] += int(request.POST['quantity'])
        request.session['total_amount'] += float(request.session['price'])
    return redirect('/checkout')

def checkout(request):
    return render(request,'amadon_app/checkout.html')
def clear(request):
    request.session.clear()
    return redirect('/')
