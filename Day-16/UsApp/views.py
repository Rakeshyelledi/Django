from django.shortcuts import render
from django.http import HttpResponse
from UsApp.forms import UsReg
from django.contrib.auth.models import User

# Create your views here.

def home(request):
#	return HttpResponse("Hi Welcome User")
	return render(request,'html/home.html')

def abts(request):
	return render(request,'html/about.html')

def cnt(request):
	return render(request,'html/contact.html')

def regs(request):
	if request.method == "POST":
		t = UsReg(request.POST)
		if t.is_valid():
			t.save()
	t = UsReg()
	return render(request,'html/register.html',{'y':t})