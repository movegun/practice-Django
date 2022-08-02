from re import template
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def login_ok(request):
    print("hi")