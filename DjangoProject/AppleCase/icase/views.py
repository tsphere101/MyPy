from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def hello(request):
    # return HttpResponse("HelloWorld")
    tags = ['น้ำตก', 'Nature', 'Rain']
    return render(request, 'index.html', {'name': 'บทความ', 'author': 'topfee', 'tags': tags,'ratings':4})
