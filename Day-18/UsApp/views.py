from django.shortcuts import render,redirect
from django.http import HttpResponse
from UsApp.forms import UsReg
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Djprjct import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
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
			return redirect('/login')
	t = UsReg()
	return render(request,'html/register.html',{'y':t})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def mailsend(request):
	if request.method == "POST":
		rec = request.POST["sndml"]
		sub = request.POST["subject"]
		msg = request.POST["messg"]
		sd = settings.EMAIL_HOST_USER
		t = send_mail(sub,msg,sd,[rec])
		if t == 1:
			return redirect("/mail")
		return HttpResponse("Didnt send mail to particular person")
	return render(request,'html/mailsending.html')