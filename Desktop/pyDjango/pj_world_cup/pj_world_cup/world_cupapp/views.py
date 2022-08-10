from re import template
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.db.models import Max, Min, Avg, Sum

import world_cupapp.models as models

from .models import *
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
            request.session['login_ok_user'] = login_user.username
        else:
            #아이디만 맞음
            result = 1
    else:pass            
    context={
        'result':result,
    }
    # print(result)
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
    # print(id,username,pwd)
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
    # print(Comment_test.objects.all().values())
    # 스트링값 받아서 models에 이름과 비교해서 가져오기 제발.
    # import inspect
    # for empty, obj in inspect.getmembers(models): #foo모듈의 class받아옴
    #     if inspect.isclass(obj):
    #         # if (obj.__name__=='Comment_room' or obj.__name__=='Member'or obj.__name__=='Ranking' or obj.__name__=='Brand_member'):
    #         #     pass
    #         # else :
    #         print(obj.__name__)
                            
    # theme의 값이 같은것 들의 win_num을 더하고 그 값을 'total_play'컬럼으로 지정하고 줄세워라
    # 게임플레이가 많은 순으로 정렬을 해두고 밑에 for문 들어가려고...
    list_total_play = All_url.objects.values('theme').annotate(total_play=Sum('win_num')).order_by('-total_play')
    #print("list_total_play :",type(list_total_play),list_total_play)
    #[{'theme': 'pokemon', 'total_play': 52},
    # {'theme': 'celeb', 'total_play': 26},
    # {'theme': 'food', 'total_play': 6},
    # {'theme': 'vegetable', 'total_play': 0}]
    
    list_first_by_theme=[]
    for theme_row in list_total_play:
        list_first_by_theme.append(All_url.objects.all().filter(theme=theme_row['theme']).order_by('-win_num').first())
        # for문 1바퀴 theme가 pokemon인 것들을 '-win_num'으로 줄세우고 첫번째 row
        # for문 2바퀴 theme가 celeb 것들을 '-win_num'으로 줄세우고 첫번째 row
        # for문 3바퀴 theme가 food 것들을 '-win_num'으로 줄세우고 첫번째 row
        # for문 4바퀴 theme가 vegetable 것들을 '-win_num'으로 줄세우고 첫번째 row
    
    print(list_first_by_theme[0].theme)
    #print(list_first_by_theme) 
    #[<All_url: pokemon 피카츄>, <All_url: celeb 오마이걸>, <All_url: food 김치찌개>, <All_url: vegetable 버섯>]
                
    context={
        'list_first_by_theme':list_first_by_theme,
    }
    
    return HttpResponse(template.render(context, request))

def logout(request):
    if request.session.get('login_ok_user'):
        request.session.clear()        
    return redirect("/")
    
def winner(request,selected_theme,selected_name):
    template = loader.get_template('winner.html')
    
    #주소창의 theme와 name을 통해 object를 찾음
    winner_row = All_url.objects.get(theme=selected_theme,name=selected_name)
    
    
    # 해당 object 의 win_num 업데이트 시켜줌
    All_url.update_win_num(winner_row)
    
    context={
        'winner_row' : winner_row,
    }    
    
    return HttpResponse(template.render(context, request))

def ranking(request,selected_theme):
    comment_objects = Comment_test.objects.filter(theme=selected_theme).order_by('-date')
    # print(comment_objects.values())
    
    if request.method == 'POST':
        if "comment" in request.POST:
            new_comment = request.POST['comment']
            if len(new_comment)==0:pass
            else:
                username = request.session['login_ok_user']
                Comment_test(username=username,theme=selected_theme,comment=new_comment).save()            

        elif "comment_order_num" in request.POST:
            comment_order_num=request.POST['comment_order_num']                        
            selected_comment_object=Comment_test.objects.get(comment_num=comment_order_num)
            Comment_test.update_hit_num(selected_comment_object)
            
        elif "lately" in request.POST:
            comment_objects = Comment_test.objects.filter(theme=selected_theme).order_by('date')            
        elif "popular" in request.POST:
            comment_objects = Comment_test.objects.filter(theme=selected_theme).order_by('-hit_num')
        elif "unpopular" in request.POST:
            comment_objects = Comment_test.objects.filter(theme=selected_theme).order_by('hit_num')    
        
    else:pass
    
    
    template = loader.get_template('ranking.html')    
    # 해당 theme 의 wim_num으로 줄세워서 리스트에 담기
    list_ranking_objects = All_url.objects.all().filter(theme=selected_theme).order_by('-win_num')    
    # print("11111",len(list_ranking_objects))
    
    # 해당 theme 의 총 플레이 수 구하기
    list_object = All_url.objects.filter(theme=selected_theme).values('theme').annotate(total_play=Sum('win_num'))
    #[{'theme': 'pokemon', 'total_play': 52}]    
    theme_total_play = list_object[0]['total_play']
    # print(theme_total_play)
    
    # rate를 담은 list를 만들고 zip 해서 보내자
    win_rates=[]
    
    for x in list_ranking_objects:
        try:
            win_rates.append(round(x.win_num/theme_total_play,2)*100)
        except ZeroDivisionError:
            win_rates.append(0)
        
    context = {
        'zipped_list_ranking_objects' : zip(list_ranking_objects, win_rates),        
        'selected_theme' : selected_theme,
        'theme_total_play' :theme_total_play,
        'comment_objects':comment_objects,
        
    }    
    return HttpResponse(template.render(context, request))

def modal(request,selected_theme):
    template = loader.get_template('modal.html')
    
    # print("themethemethemetheme",selected_theme)
    context = {
        'selected_theme':selected_theme        
    }
 
    
    return HttpResponse(template.render(context, request))

def test(request):
    template = loader.get_template('comment_test.html')
    theme='안녕'
    context = {
        'theme':theme        
    }    
    return HttpResponse(template.render(context, request))

def play(request,selected_theme,selected_rounds):
    template = loader.get_template('test.html')
    
    play_base = All_url.objects.filter(theme=selected_theme).order_by('?')[:selected_rounds]
    # for i in range(1,rounds+1):
    #     play_base.append(All_url.objects.filter(theme=theme).order_by('?')[:2])
    # print(play_base)    
    context={
        'play_base':play_base,
        'selected_rounds':selected_rounds,
        'selected_theme':selected_theme,
    }       
    return HttpResponse(template.render(context, request))