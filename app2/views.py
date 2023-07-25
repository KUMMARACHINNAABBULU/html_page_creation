from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def third(request):
    return render(request,'third.html')
def fourth(request):
    return render(request,'fourth.html')
def abbulu2(request):
    return HttpResponse('marathahalli')