from xml.etree.ElementInclude import include
import os
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:blog_id>",views.stranica,name="stranica"),
    path("pocetna/",views.pocetna,name="pocetna"),
    #path("<int:blog_id>",views.submit,name="submit"),

    


]
