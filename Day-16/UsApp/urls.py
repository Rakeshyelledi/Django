from django.urls import path,include
from UsApp import views

urlpatterns = [
    path('',views.home,name="hm"),
    path('about/',views.abts,name="abt"),
    path('contact/',views.cnt,name="con"),
    path('register/',views.regs,name="reg"),
]
