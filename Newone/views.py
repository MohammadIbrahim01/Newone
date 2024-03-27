from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from django.shortcuts import render,redirect


def aboutUs1(request):
    return HttpResponse('hai')

def indexqqq(request):
   
     return render(request,'index.html')