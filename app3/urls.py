from django.urls import path
from app3.views import *

app_name='something'
urlpatterns=[
    path('fifth/',fifth,name='fifth'),
    path('sixth/',sixth,name='sixth'),
    path('abbulu3/',abbulu3,name='abbulu3')
]