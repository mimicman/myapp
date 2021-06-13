from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template_name = "index.html" # templates以下のパスを書く
    return render(request,template_name)
    #return HttpResponse("Hello, world. You're at the polls index.")