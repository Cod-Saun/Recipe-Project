from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "body":"CINS 465 Hello World! Template",
    }
    return render(request,"index.html", context=context)
