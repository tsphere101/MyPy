from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("This is home page.")

    return render(request,'index.html',{'name':'THIS IS NAME','title':'HOME'})

