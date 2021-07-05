from django.http import HttpResponse
import os
import datetime
import subprocess
import tempfile
from collections import deque
import sqlite3
import cv2
import time
from PIL import Image
import cv2
import PIL.ImageOps    
from django.views.generic import ListView
import glob
import numpy as np
from django.shortcuts import render, redirect
from numpy.core.fromnumeric import size
from numpy.lib.type_check import imag
from .forms import *
from .models import *
import matplotlib.pyplot as plt
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
import json  
def normal_monk_smart(request,img):
    s_study_wrong=str(request.POST)
    s_study_w1rong=request.POST
    data_django_1="email"
    path_1hai = settings.MEDIA_ROOT
    x_user_pong=str(request.user)
    p_t1=path_1hai+'\doto\monk.json'
    q_t1=path_1hai+'\doto\monk1.json'
    r_t1=path_1hai+'\doto\monk2.json'
    location='/media/imagrinprocessing/'
    with open(p_t1) as fz:
        temp_user_pong=json.load(fz)
    with open(q_t1) as fz:
        temp1_user_pong=json.load(fz)
    with open(r_t1) as fz:
        temp2_user_pong=json.load(fz)
    workable_hardworking=str(request.POST['description'])
    straight=Image.fromarray(img)
    lackmonk=Image.open(path_1hai+temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][-1].replace("/media",""))
    if np.array_equal(np.array(lackmonk),img)!=True:
        for i in temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][2]:
            if   os.path.isfile(path_1hai+i.replace("/media","")):
                os.remove(path_1hai+i.replace("/media",""))
        l1=img.shape
        size = (1200,720)
        box1 = (0,0,l1[1],l1[0])
        straight=straight.resize(size,box=box1)
        remem=temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][0]
        straight.save(path_1hai+"/imagrinprocessing/timefrax__c"+temp2_user_pong[x_user_pong]+temp2_user_pong[x_user_pong]+str(remem)+".png")
        temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1].append(location+"timefrax__c"+temp2_user_pong[x_user_pong]+temp2_user_pong[x_user_pong]+str(remem)+".png")
        temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][0]=temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][0]+1
        with open(q_t1,"w") as fz:
            json.dump(temp1_user_pong,fz,indent=2)
        return render (request,"polls/compiler.html", {"workable_hardworking":workable_hardworking,"lowest_mall":temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][-1],"kong_strong":temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][0]}) 
    return None

def imagecontainer1(l,m):
    l=np.array(l)
    m=np.array(m)
    l1=l.shape
    m1=m.shape
    l2=len(l1)
    m2=len(m1)
    if l2>m2:
        l=cv2.cvtColor(l, cv2.COLOR_BGR2GRAY)
    elif m2>l2:
        m=cv2.cvtColor(m, cv2.COLOR_BGR2GRAY)
    l=Image.fromarray(l)
    m=Image.fromarray(m)
    size = (1200,720)
    box1 = (0,0,l1[1],l1[0])
    box2=(0,0,m1[1],m1[0])
    l=np.array(l.resize(size,box=box1))
    m=np.array(m.resize(size,box=box2))
    result=l*l
    result[result>255]=255
    result[result<0]=0
    result=Image.fromarray(result)
    return result
def imagecontainer(l,m):
    l=np.array(l)
    m=np.array(m)
    l1=l.shape
    m1=m.shape
    l2=len(l1)
    m2=len(m1)
    if l2>m2:
        l=cv2.cvtColor(l, cv2.COLOR_BGR2GRAY)
    elif m2>l2:
        m=cv2.cvtColor(m, cv2.COLOR_BGR2GRAY)
    l=Image.fromarray(l)
    m=Image.fromarray(m)
    size = (1200,720)
    box1 = (0,0,l1[1],l1[0])
    box2=(0,0,m1[1],m1[0])
    l=np.array(l.resize(size,box=box1))
    m=np.array(m.resize(size,box=box2))
    result=l+m
    result[result>255]=255
    result[result<0]=0
    result=Image.fromarray(result)
    return result
def index(request):
    if request.method == 'POST':
        form = HotelForm( request.POST,request.FILES)
        path = settings.MEDIA_ROOT
        location="/media/images/"
        x=str(request.user)
        p=path+'\doto\monk.json'
        data="email"
        if form.is_valid():
            arr=os.listdir(path+"/images/")
            imp={i:0 for i in arr}
            form.save()
            arr=deque(os.listdir(path+"/images/"))
            with open(p) as fz:
                temp=json.load(fz)
            while(arr):
                if arr[0] not in imp:
                    temp[data][x][location+arr[0]]=str(datetime.datetime.today())
                    break
                arr.popleft()
            with open(p,"w") as fz:
                json.dump(temp,fz,indent=2)
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'polls/honk.html', {'form' : form})
def success(request):
    data="email"
    klm=[]
    path = settings.MEDIA_ROOT
    x=str(request.user)
    p=path+'\doto\monk.json'
    q=path+'\doto\monk1.json'
    with open(p) as fz:
        temp=json.load(fz)
    if x not in temp[data]:
        temp[data][x]={}
    pl=temp[data][x]
    with open(q) as fz:
        temp1=json.load(fz)
    with open(p,"w") as fz:
        json.dump(temp,fz,indent=2)
    if x not in temp1 or len(temp1[x])==0:
        temp1[x]={"NOFILES":0}
    return render(request,"polls/success.html",{"kno":pl,"lo":"Do the selection for further processing","klm":temp1[x]})
def loginPage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('honk')
        else:
            messages.info(request, 'Username or password incorrect')
    context={}
    return render(request,'registration/login.html',context)
def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('honk')
    else:
        form =CustomUserCreationForm() 
    context={"form":form}
    return render(request,'registration/register.html',context)
def work(request):
    if 'same1' in request.POST and 'same' in request.POST:
        if request.POST['same1']=="SELECT IMAGE":
            data="email"
            path = settings.MEDIA_ROOT
            x=str(request.user)
            p=path+'\doto\monk.json'
            q=path+'\doto\monk1.json'
            r=path+'\doto\monk2.json'
            with open(p) as fz:
                temp=json.load(fz)
            z_location=str(request.POST)
            dc=len(z_location)
            t=0
            s=""
            for i in range(dc):
                if z_location[i-4:i]=="same" or t==1:
                    t=1
                    if z_location[i]=="]":
                        break
                    s=s+z_location[i]
            s=s[4:]
            s=s.replace("'","")
            f=list(s.split(","))
            with open(q) as fz:
                temp1=json.load(fz)
            if x not in temp1 :
                temp1[x]={}
                tfg="file0"
            else:
                try:
                    rf=max(temp1[x]).replace("file","")
                    tfg="file"+str(int(rf)+1)
                except:
                    tfg="file0"
            with open(r) as fz:
                temp2=json.load(fz)
            temp2[x]=tfg
            with open(r,"w") as fz:
                json.dump(temp2,fz,indent=2)
            temp1[x][tfg]=[{i.replace(" ",""):str(datetime.datetime.today()) for i in f},[0],[]]
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
            return render(request,'polls/image.html',{"gallary":temp[data][x],"pics":[temp1[x][tfg][0]]})
        elif request.POST['same1']=="DELETE IMAGE":
            data="email"
            path = settings.MEDIA_ROOT
            x=str(request.user)
            p=path+'\doto\monk.json'
            q=path+'\doto\monk1.json'
            with open(p) as fz:
                temp=json.load(fz)
            z_location=str(request.POST)
            dc=len(z_location)
            t=0
            s=""
            for i in range(dc):
                if z_location[i-4:i]=="same" or t==1:
                    t=1
                    if z_location[i]=="]":
                        break
                    s=s+z_location[i]
            s=s[4:]
            s=s.replace("'","")
            f=list(s.split(","))
            for i in f:
                zxv=i.replace(" ","")
                if zxv in temp[data][x]:
                    temp[data][x].pop(zxv)
                    s=path+zxv.replace("media/","")
                    os.remove(s)
            with open(p,"w") as fz:
                json.dump(temp,fz,indent=2)
            with open(q) as fz:
                temp1=json.load(fz)
            if x not in temp1 or len(temp1[x])==0:
                temp1[x]={"NOFILES":0}
            return render(request,"polls/success.html",{"kno":temp[data][x],"lo":" DELETION DONE SELECT ANOTHER ONE TO DELETE","klm":temp1[x]})
    else:
        if "cars" in request.POST:
            comp=request.POST["cars"]
            if str(comp)!="NOFILES":
                if "same2" in str(request.POST) and  request.POST['same2']=="SELECT FILE":

                    data="email"
                    path = settings.MEDIA_ROOT
                    x=str(request.user)
                    p=path+'\doto\monk.json'
                    q=path+'\doto\monk1.json'
                    r=path+'\doto\monk2.json'
                    with open(p) as fz:
                        temp=json.load(fz)
                    with open(q) as fz:
                        temp1=json.load(fz)
                    with open(r) as fz:
                        temp2=json.load(fz)
                    temp2[x]=comp
                    with open(r,"w") as fz:
                        json.dump(temp2,fz,indent=2)
                    vlb={}
                    conter=0
                    if comp in temp1[x]:
                        for i in  temp1[x][comp][0]:
                            vlb[i]="gh"+str(conter)
                            conter+=1
                    return render(request,'polls/image.html',{"gallary":temp[data][x],"pics":[vlb],"picsimp":[temp1[x][comp][1][-1]]})
                elif "same2" in str(request.POST) and request.POST['same2']=="DELETE FILE":
                    
                    data="email"
                    x=str(request.user)
                    path = settings.MEDIA_ROOT
                    p=path+'\doto\monk.json'
                    q=path+'\doto\monk1.json'
                    r=path+'\doto\monk2.json'
                    with open(p) as fz:
                        temp=json.load(fz)
                    with open(q) as fz:
                        temp1=json.load(fz)  
                    with open(r) as fz:
                        temp2=json.load(fz)
                    temp2[x]=comp
                    if comp in temp1[x]:
                        for i in temp1[x][temp2[x]][1]:
                            if str(i).isnumeric()!=True:
                                os.remove(path+i.replace("/media",""))
                        for i in temp1[x][temp2[x]][2]:
                            os.remove(path+i.replace("/media",""))
                        temp1[x].pop(comp)
                    with open(q,"w") as fz:
                        json.dump(temp1,fz,indent=2) 
                    if len(temp1[x])==0:
                        temp1[x]={"NOFILES":0}
                    return render(request,"polls/success.html",{"kno":temp[data][x],"lo":"SELECT ANOTHER FILE TO DELETE","klm":temp1[x]})
        data="email"
        path = settings.MEDIA_ROOT
        x=str(request.user)
        p=path+'\doto\monk.json'
        q=path+'\doto\monk1.json'
        with open(p) as fz:
            temp=json.load(fz)
        pl=temp[data][x]
        with open(q) as fz:
            temp=json.load(fz)
        if x not in temp:
            temp[x]={"NOFILES":0}
        return render(request,"polls/success.html",{"kno":pl,"lo":"PLEASE SELECT IMAGE FOR ANALYSIS","klm":temp[x]})
def image(request):
    forall=request.POST
    need1=str(forall)
    data="email"
    path = settings.MEDIA_ROOT
    x=str(request.user)
    p=path+'\doto\monk.json'
    q=path+'\doto\monk1.json'
    r=path+'\doto\monk2.json'
    location='/media/imagrinprocessing/'
    with open(p) as fz:
        temp=json.load(fz)
    with open(q) as fz:
        temp1=json.load(fz)
    with open(r) as fz:
        temp2=json.load(fz)    
    if "power" in need1 and "power_c" in need1:
        s=""
        t=0
        for i in range(len(need1)):
            if need1[i-7:i]=="power_c" or t==1:
                t=1
                if need1[i]=="]":
                        break
                s=s+need1[i]
        s=s[4:]
        s=s.replace("'","")
        need=list(s.split(","))
        for i in need:
            zcv=i.replace(" ","")
            if zcv not in temp1[x][temp2[x]][0]:
                temp1[x][temp2[x]][0][zcv]=str(datetime.datetime.today())
        with open(q,"w") as fz:
            json.dump(temp1,fz,indent=2)
    elif "power1" in need1:
        if "samebh" in need1:
            s=""
            t=0
            for i in range(len(need1)):
                if need1[i-6:i]=="samebh" or t==1:
                    t=1
                    if need1[i]=="]":
                        break
                    s=s+need1[i]
            s=s[4:]
            s=s.replace("'","")
            f=list(s.split(","))
            for i in f:
                a=str(i.replace(" ",""))
                if a in temp1[x][temp2[x]][0]:
                    temp1[x][temp2[x]][0].pop(a)
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
    elif "power2" in need1:
        if "samebh" in need1:
            for i in temp1[x][temp2[x]][2]:
                if   os.path.isfile(path+i.replace("/media","")):
                    os.remove(path+i.replace("/media",""))
            temp1[x][temp2[x]][2]=[]
            s=""
            t=0
            for i in range(len(need1)):
                if need1[i-6:i]=="samebh" or t==1:
                    t=1
                    if need1[i]=="]":
                        break
                    s=s+need1[i]
            s=s[4:]
            s=s.replace("'","")
            f=list(s.split(","))
            position=str(temp1[x][temp2[x]][1][0])
            tochange=temp2[x]
            task=0
            for i in f:
                pn=i.replace(" ","")
                if position!="0":
                    if task!=0:
                        pcv=Image.open(path+pn.replace("/media",""))
                        star=Image.open(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        monk=imagecontainer(pcv,star)
                        monk.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                    else:
                        pcv=Image.open(path+pn.replace("/media",""))
                        star=Image.open(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+str(int(position)-1)+".png")
                        monk=imagecontainer(pcv,star)
                        monk.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        task=task+1
                else:
                    if task!=0:
                        pcv=Image.open(path+pn.replace("/media",""))
                        star=Image.open(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        monk=imagecontainer(pcv,star)
                        monk.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                    else:
                        pcv=Image.open(path+pn.replace("/media",""))
                        l1=np.array(pcv).shape
                        size981 = (1200,720)
                        box121 = (0,0,l1[1],l1[0])
                        pcv=pcv.resize(size981,box=box121)
                        pcv.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        task=task+1
            temp1[x][temp2[x]][1][0]=int(position)+1
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+tochange+tochange+position+".png")
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)    
    elif "power3" in need1:
        place=temp1[x][temp2[x]][1][0]
        if place!=0:
                temp1[x][temp2[x]][2].append(temp1[x][temp2[x]][1][-1])
                temp1[x][temp2[x]][1].pop(-1)
                temp1[x][temp2[x]][1][0]=place-1
                with open(q,"w") as fz:
                    json.dump(temp1,fz,indent=2)   
    elif "power4" in need1:
        if len(temp1[x][temp2[x]][2])!=0:
            temp1[x][temp2[x]][1].append(temp1[x][temp2[x]][2][-1])
            temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
            temp1[x][temp2[x]][2].pop(-1)
            with open(q,"w") as fz:
                    json.dump(temp1,fz,indent=2)  
    elif "power6" in need1:
        for i in temp1[x][temp2[x]][2]:
            if   os.path.isfile(path+i.replace("/media","")):
                os.remove(path+i.replace("/media",""))
        temp1[x][temp2[x]][2]=[]
        posts=temp1[x][temp2[x]][1][-1]
        remem=temp1[x][temp2[x]][1][0]
        if posts!=0:
            image1=np.array(Image.open(path+posts.replace("/media","")))
            image1=cv2.bilateralFilter(image1,int(forall['power5']),int(forall['power51']),int(forall['power52']))
            image1=Image.fromarray(image1)
            image1.save(path+"/imagrinprocessing/timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
    elif "power8" in need1 and "power7" in need1 and "power71" in need1:
        for i in temp1[x][temp2[x]][2]:
            if   os.path.isfile(path+i.replace("/media","")):
                os.remove(path+i.replace("/media",""))
        temp1[x][temp2[x]][2]=[]
        posts=temp1[x][temp2[x]][1][-1]
        remem=temp1[x][temp2[x]][1][0]
        if posts!=0:
            image1=np.array(Image.open(path+posts.replace("/media","")))
            image1= cv2.Canny(image1,int(forall['power7']),int(forall['power71']))
            image1=Image.fromarray(image1)
            image1.save(path+"/imagrinprocessing/timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
    elif "power9" in need1 and 'power81' in need1 and 'power82' in need1:
        posts=temp1[x][temp2[x]][1][-1]
        remem=temp1[x][temp2[x]][1][0]
        if posts!=0:
            image2=np.array(Image.open(path+posts.replace("/media","")))
            imgcon=Image.fromarray(image2)
            l1i=image2.shape
            size = (int(forall['power81']),int(forall['power82']))
            box1 = (0,0,l1i[1],l1i[0])
            imgcon.resize(size,box=box1)
            imgcon.save(path+'/images/'+posts.replace("media/imagrinprocessing/",""))
            temp[data][x]['/media/images/'+posts.replace("media/imagrinprocessing/","")]=str(datetime.datetime.today())
            with open(p,"w") as fz:
                json.dump(temp,fz,indent=2)
    elif "power91" in need1:
        for i in temp1[x][temp2[x]][2]: 
            if   os.path.isfile(path+i.replace("/media","")):
                os.remove(path+i.replace("/media",""))
        temp1[x][temp2[x]][2]=[]
        posts=temp1[x][temp2[x]][1][-1]
        remem=temp1[x][temp2[x]][1][0]
        if posts!=0:
            image3=Image.open(path+posts.replace("/media",""))
            inverted=PIL.ImageOps.invert(image3)
            inverted.save(path+"/imagrinprocessing/timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
    elif "power92" in need1:
        for i in temp1[x][temp2[x]][2]:
            if   os.path.isfile(path+i.replace("/media","")):
                os.remove(path+i.replace("/media",""))
        temp1[x][temp2[x]][2]=[]
        posts=temp1[x][temp2[x]][1][-1]
        remem=temp1[x][temp2[x]][1][0]
        if posts!=0:
            image3=Image.open(path+posts.replace("/media",""))
            inverted=PIL.ImageOps.grayscale(image3)
            inverted.save(path+"/imagrinprocessing/timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
    elif "power93" in need1:
        for i in temp1[x][temp2[x]][2]:
            if   os.path.isfile(path+i.replace("/media","")):
                os.remove(path+i.replace("/media",""))
        temp1[x][temp2[x]][2]=[]
        posts=temp1[x][temp2[x]][1][-1]
        remem=temp1[x][temp2[x]][1][0]
        if posts!=0:
            image3=np.array(Image.open(path+posts.replace("/media","")))
            image3=cv2.bitwise_not(image3)
            inverted=Image.fromarray(image3)
            inverted.save(path+"/imagrinprocessing/timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
    elif "wower101" in need1 and "samebh" in  need1:
            for i in temp1[x][temp2[x]][2]:
                if   os.path.isfile(path+i.replace("/media","")):
                    os.remove(path+i.replace("/media",""))
            temp1[x][temp2[x]][2]=[]
            s=""
            t=0
            for i in range(len(need1)):
                if need1[i-6:i]=="samebh" or t==1:
                    t=1
                    if need1[i]=="]":
                        break
                    s=s+need1[i]
            s=s[4:]
            s=s.replace("'","")
            f=list(s.split(","))
            position=str(temp1[x][temp2[x]][1][0])
            tochange=temp2[x]
            task=0
            for i in f:
                pn=i.replace(" ","")
                if position!="0":
                    if task!=0:
                        pcv=Image.open(path+pn.replace("/media",""))
                        star=Image.open(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        monk=imagecontainer1(pcv,star)
                        monk.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                    else:
                        pcv=Image.open(path+pn.replace("/media",""))
                        star=Image.open(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+str(int(position)-1)+".png")
                        monk=imagecontainer1(pcv,star)
                        monk.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        task=task+1
                else:
                    if task!=0:
                        print(path+pn.replace("/media",""))
                        pcv=Image.open(path+pn.replace("/media",""))
                        star=Image.open(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        monk=imagecontainer1(pcv,star)
                        monk.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                    else:
                        pcv=Image.open(path+pn.replace("/media",""))
                        l1=np.array(pcv).shape
                        size98 = (1200,720)
                        box12 = (0,0,l1[1],l1[0])
                        pcv=pcv.resize(size98,box=box12)
                        pcv.save(path+"/imagrinprocessing/timefrax__c"+tochange+tochange+position+".png")
                        task=task+1
            temp1[x][temp2[x]][1][0]=int(position)+1
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+tochange+tochange+position+".png")
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)    
    elif "wong13" in need1: 
        try:
            for i in temp1[x][temp2[x]][2]:
                if   os.path.isfile(path+i.replace("/media","")):
                    os.remove(path+i.replace("/media",""))
            temp1[x][temp2[x]][2]=[]
            posts=temp1[x][temp2[x]][1][-1]
            remem=temp1[x][temp2[x]][1][0]
            imgcov=eval("np.array("+str(forall['wong134'])+")")
            l=imgcov.shape
            imgcov=Image.fromarray(np.array(imgcov))
            box1=(0,0,l[1],l[0])
            size1=(1200,720)
            imgcov=imgcov.resize(size1,box=box1)
            imgcov.save(path+"/imagrinprocessing/timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1].append(location+"timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
            temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
            with open(q,"w") as fz:
                json.dump(temp1,fz,indent=2)
        except:
            pass
    elif "pwxong13" in need1 and "pwxong134" in need1 :
        for i in temp1[x][temp2[x]][2]:
            if   os.path.isfile(path+i.replace("/media","")):
                os.remove(path+i.replace("/media",""))
        temp1[x][temp2[x]][2]=[]
        remem=temp1[x][temp2[x]][1][0]
        if temp1[x][temp2[x]][1][-1]!=0:
            try:
                srcimg=np.array(Image.open(path+temp1[x][temp2[x]][1][-1].replace("/media","")))
                straight=eval(str(forall['pwxong134']))
                straight=Image.fromarray(straight)
                straight.save(path+"/imagrinprocessing/timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
                temp1[x][temp2[x]][1].append(location+"timefrax__c"+temp2[x]+temp2[x]+str(remem)+".png")
                temp1[x][temp2[x]][1][0]=temp1[x][temp2[x]][1][0]+1
                with open(q,"w") as fz:
                    json.dump(temp1,fz,indent=2)
            except:
                pass


        
    vlb={}
    conter=0
    if temp2[x] in temp1[x]:
        for i in  temp1[x][temp2[x]][0]:
            vlb[i]="gh"+str(conter)
            conter+=1
    return render(request,'polls/image.html',{"gallary":temp[data][x],"pics":[vlb],"picsimp":[temp1[x][temp2[x]][1][-1]]})
def compiler(request):
    
    s_study_wrong=str(request.POST)
    s_study_w1rong=request.POST
    data_django_1="email"
    workable_hardworking=""
    workflow=[]
    path_1hai = settings.MEDIA_ROOT
    x_user_pong=str(request.user)
    p_t1=path_1hai+'\doto\monk.json'
    q_t1=path_1hai+'\doto\monk1.json'
    r_t1=path_1hai+'\doto\monk2.json'
    location_sfd_1='/media/imagrinprocessing/'
    with open(p_t1) as fz:
        temp_user_pong=json.load(fz)
    with open(q_t1) as fz:
        temp1_user_pong=json.load(fz)
    with open(r_t1) as fz:
        temp2_user_pong=json.load(fz)

    if temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][-1]!=0:
        for i in temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][0]:
            z_long_xcv=Image.open(path_1hai+i.replace("/media",""))
            l1=np.array(z_long_xcv).shape
            z_long_xcv=np.array(z_long_xcv.resize((1200,720),box=(0,0,l1[1],l1[0])))
            workflow.append(z_long_xcv)
        img=np.array(Image.open(path_1hai+temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][-1].replace("/media","")))
        if "description" in s_study_w1rong and "return" in s_study_w1rong:
            workable_hardworking=str(request.POST['description'])
            exec(workable_hardworking)
    return render(request,"polls/compiler.html",{"workable_hardworking":workable_hardworking,"lowest_mall":temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][1][-1],"kong_strong":temp1_user_pong[x_user_pong][temp2_user_pong[x_user_pong]][0]} )