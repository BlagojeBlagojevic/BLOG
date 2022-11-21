import imp
from django.contrib import admin
from BLOG.models import Blog,Komentar
# Register your models here.



admin.site.register(Blog)
admin.site.register(Komentar)
