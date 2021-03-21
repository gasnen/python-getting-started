from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import menu as Menucreator
from django.contrib.auth import logout,login
from django.contrib.auth.models import User,Permission

def userauth(request):
    if request.user.is_authenticated: 
        # add here user profile valid
        return True
    else:
        pass
    return False
def lout(request):
    logout(request)
    return HttpResponseRedirect('/')
def userinfo(request):
    menuarr=[]
    menuarr.clear
    if userauth(request):
        print("user")
        menuarr=[]
        print("create menu")
        menuarr=Menucreator.createmenu(True)

    else: 
        menuarr=[]
        menuarr=Menucreator.createmenu(False) 

    ret=request.user
    user=User.objects.filter(username=request.user)
    print(user)    
    print (ret)
    return render(request, 'index.html',{"menu":menuarr
                                         ,"ret":ret,})
def index(request):
    menuarr=[]
    menuarr.clear
    if userauth(request):
        print("user")
        menuarr=[]
        print("create menu")
        menuarr=Menucreator.createmenu(True)
    else:  
        menuarr=[]
        menuarr=Menucreator.createmenu(False)
    print(menuarr)
    return render(request, 'index.html',{"menu":menuarr,}
                                                       )