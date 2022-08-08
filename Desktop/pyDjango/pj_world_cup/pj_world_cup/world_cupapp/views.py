from re import template
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.db.models import Max, Min, Avg

import world_cupapp.models as models
import sys, inspect



from .models import All_url, Member,Urls,Ranking
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
    # print("하이ㄴ")    
    # print("확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용",All_url._meta.get_fields())    
    rank_dict = Ranking.objects.all().aggregate(rank=Max('rank'))
    max_num=rank_dict['rank']
    first_object=Ranking.objects.get(rank=max_num)
    print(first_object)
    
    rank_object = All_url.objects.get(name=first_object)
    
    context={
        'rank_object':rank_object,        
    }
    
    return HttpResponse(template.render(context, request))

def logout(request):
    if request.session.get('login_ok_user'):
        request.session.clear()        
    return redirect("/")


def two_imgs(request):
    template = loader.get_template('two_imgs.html')
    
    all_url = Urls.objects.all()
    context={
        'all_url':all_url,        
    }           
    
    
    # print(all_url)
    return HttpResponse(template.render(context, request))

def testpage(request):
    template = loader.get_template('testpage.html')
    
    
    all_url = Urls.objects.all()
    context={
        'all_url':all_url,        
    }           
    
    
    
    
    return HttpResponse(template.render(context, request))
    
def winner(request):
    template = loader.get_template('winner.html')    
    name = request.POST.get('rankname',None)
    print("name",name)
    #rank = request.POST.get('ranking',None)
    
    try:
        if Ranking.objects.get(name=name):
            Ranking.update_rank(Ranking.objects.get(name=name))            
    
    except Ranking.DoesNotExist:
        print("없어서 row 생성")
        Ranking(name=name).save()
        Ranking.update_rank(Ranking.objects.get(name=name))
    
    return HttpResponse(template.render({}, request))

def ranking(request):
    template = loader.get_template('ranking.html')
    all_rank = Ranking.objects.all().order_by('-rank')
    
    context = {
        'all_rank':all_rank,        
    }
    
    
    
    return HttpResponse(template.render(context, request))

def boot(request):
    template = loader.get_template('boot.html')
    all_url = Urls.objects.all()
    context={
        'all_url':all_url,        
    }         
    
    
    return HttpResponse(template.render(context, request))

def modal(request,theme):
    template = loader.get_template('modal.html')
    # print("확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용확인용")
    # print(type(inspect.getmembers(models)))
    
    print("themethemethemetheme",theme)
    context = {
        'theme':theme        
    }
 
    
    for empty, obj in inspect.getmembers(models): #foo모듈의 class받아옴
        if inspect.isclass(obj):
            if (obj.__name__=='Comment_room' or obj.__name__=='Member'or obj.__name__=='Ranking' or obj.__name__=='Brand_member'):
                pass
            else :
                print(obj.__name__)
    return HttpResponse(template.render(context, request))

def test(request):
    template = loader.get_template('test.html')
    theme='안녕'
    context = {
        'theme':theme        
    }    
    return HttpResponse(template.render(context, request))

# def celeb(request):
#     template = loader.get_template('testpage.html')    
#     all_url = Urls.objects.all()
#     context={
#         'all_url':all_url,        
#     }           
#     return HttpResponse(template.render(context, request))


    
    