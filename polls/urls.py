# ! /usr/ bin/python 
# -*- coding : UTF- 8 -*-

from django.urls import path

from . import  views

urlpatterns=[
    path('',views.index,name='index'),
]