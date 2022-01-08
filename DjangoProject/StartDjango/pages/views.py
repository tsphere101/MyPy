from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args,**kwargs): # *args **kwargs
    context = {
        'title':'iCase'
    } 
    return render(request,'index.html',context)

def home2_view(request,*args,**kwargs):
    return render(request,'home_test.html')

def ct_view(request,*args,**kwargs):
    my_context = {
        'title':'CT',
         'my_nums':[7,2,3,8,3,4,5,6,12,8,5,3],
         'my_html':'<h1>Hello</h1>'
    }
    return render(request,'contractwithdb.html',my_context)