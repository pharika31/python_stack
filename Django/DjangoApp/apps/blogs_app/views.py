from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "<div >Here we will display list of blogs!!Hello, I am your first request - blogs app!</div>"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request,number):
    response = "placeholder to display blog number "+number
    return HttpResponse(response)

def edit(request,number):
    response = "placeholder to edit blog number "+number
    return HttpResponse(response)

def destroy(request,number):
    return redirect('/')
