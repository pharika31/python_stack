from django.shortcuts import render, redirect, HttpResponse
def surveys(request):
    response = "<div >Here we will display all surveys!</div>"
    return HttpResponse(response)
def new(request):
    response = "<div >placeholder for users to add a new survey!</div>"
    return HttpResponse(response)
