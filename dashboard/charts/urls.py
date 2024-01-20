from django.urls import path
from . import views
 
urlpatterns=[
    path('getnum/',views.Api.getNums, name='get-num'),
    path('getavg/',views.Api.getAvg, name='get-avg'),
    path('getgraph/',views.Api.getGraph, name='get-graph'),
    path('getdata/',views.Api.getData, name='get-data'),
]