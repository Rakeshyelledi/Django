from django.urls import path,include
from UsApp import views
from django.contrib.auth import views as v

urlpatterns = [
    path('',views.home,name="hm"),
    path('about/',views.abts,name="abt"),
    path('contact/',views.cnt,name="con"),
    path('register/',views.regs,name="reg"),
    path('login/',v.LoginView.as_view(template_name="html/login.html"),name="log"),
    path('dashboard/',views.dashboard,name="dash"),
    path('logout/',v.LogoutView.as_view(template_name="html/logout.html"),name="logo"),
    path('mail/',views.mailsend,name="ms"),
    path('profile/',views.profi,name="pf"),
    path('updateprofile/',views.updf,name="up"),

]
