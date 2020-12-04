from django.urls import path,include
from UsApp import views

urlpatterns = [
    path('',views.home),
]
