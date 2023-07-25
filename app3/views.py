from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fifth(request):
    return render(request,'fifth.html')
def sixth(request):
    return render(request,'sixth.html')
def abbulu3(request):
    return HttpResponse('come on....')