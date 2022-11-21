from asyncio.windows_events import NULL
from pickle import NONE
from pyexpat import model
from turtle import mode
from django.db import  models
from datetime import datetime
from pkg_resources import require
# Create your models here.

class Blog(models.Model):
     
     naslov=models.CharField(max_length=64,name='naslov')
     autor=models.CharField(max_length=64,name='autor')
     vrijeme_kreiranja=models.TimeField()
     tekst=models.TextField(name='tekst')
     adresa_slike=models.CharField(max_length=200,name="adresa_slike",blank=True)
     
     def __str__(self):
         return f"naslov:{self.naslov} autor:{self.autor} "



class Komentar(models.Model):

    Nik=models.CharField(max_length=64,default="NULL",name="Nik")
    komentar=models.CharField(max_length=64,default="NULL",name="komentar")
    vrijeme_komentara=models.DateField(default="NULL",name="vrijeme_komentara")
    email=models.EmailField(name='email', max_length=54,default="NULL")
    blog= models.ForeignKey(Blog, related_name='blog', on_delete=models.CASCADE)

    def __str__(self):
        return f"Komentar od {self.Nik}  u {self.vrijeme_komentara} "


