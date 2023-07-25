from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return render(request,'first.html')
def second(request):
    return render(request,'second.html')
def abbulu1(request):
    return HttpResponse('My Name Is Abbulu')