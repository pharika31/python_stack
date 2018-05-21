from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *
# Create your views here.
def index(request):
    context = {
	'date': strftime("%b %d, %Y", localtime()),
	'time':  strftime('%#I:%M %p', localtime())
	}
	
    return render(request,'times_app/index.html', context)
