from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from flask import request_started
from .models import Blog, Komentar
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class komentari(forms.Form):
    nik = forms.CharField(label='Your name', max_length=100)
    komentar=forms.CharField(label="komentar")
    vrijeme_komentara=date.today()
    email=forms.EmailField(label='Email')




# Create your views here.

def index(request):
    return render(request,'BLOG/layout.html')



def pocetna(request):
    return render(request,'BLOG/pocetna.html',{
    "Blogs" : Blog.objects.all(),})


def stranica(request,blog_id):
    blog=Blog.objects.get(pk=blog_id)    
    KOMENTARI=Komentar.objects.all().filter(blog=blog)
    if request.method == "POST":
        form = komentari(request.POST)
        if form.is_valid():
                komentar=form.cleaned_data["komentar"]
                nik=form.cleaned_data["nik"]
                email=form.cleaned_data["email"]
                #vrijeme_komentara=date.today()
                vrijeme_komentara=date.today()
                
                pom=Komentar(Nik=nik,komentar=komentar
                ,vrijeme_komentara=vrijeme_komentara,
                email=email,blog=blog)
                
               # print(pom.save())
                pom.save(force_insert=True)                
                
        
        return HttpResponseRedirect(reverse("stranica",args=(blog_id,)))

    return render(request,"BLOG/stranica.html",{
         "blog_1":blog,
         "komentari":KOMENTARI,
         "form":komentari()
        
    })
    




    





