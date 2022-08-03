from re import template
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Member
# Create your views here.

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def login_ok(request):    
    # email = request.POST['email']
    email = request.POST.get('email',None)
    # pwd = request.POST['pwd']
    pwd = request.POST.get('pwd',None)
    try:
        login_user = Member.objects.get(id=email)   # ID를 DB로부터 가져오는 과정
    except Member.DoesNotExist:
        login_user = None    
    result=0    
    if login_user !=None:
        #아이디있을때        
        if login_user.pwd == pwd:
            #아디비번까지 이맞음
            result = 2            
            request.session['login_ok_user'] = login_user.id
        else:
            #아이디만 맞음
            result = 1
    else:pass            
    context={
        'result':result,
    }           
    print(result)
    # request.session.clear()
    template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))
    
    # if result==2:
    #     template = loader.get_template('home.html')
    #     return HttpResponse(template.render(context, request))
    # else:
    #     template = loader.get_template('login.html')
    #     return HttpResponse(template.render(context, request))
    
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))
    
def register_ok(request):
    
    id = request.POST.get('userid',None)
    username = request.POST.get('username',None)
    pwd = request.POST.get('pwd1',None)
    print(id,username,pwd)
    try:
        signup_user = Member.objects.get(id=id)   # ID를 DB로부터 가져오는 과정
    except Member.DoesNotExist:
        signup_user = None
    
    result=0 #가입실패
    if signup_user==None:
        #가입신청한 아이디가 없을때 
        new_member = Member(id=id, username=username, pwd=pwd)
        new_member.save()
        result=1 # 가입성공
    else:pass
    context={
        'result':result,
    }    
    
    template = loader.get_template('register.html')
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def logout(request):
    if request.session.get('login_ok_user'):
        request.session.clear()        
    return redirect("/")
    
    