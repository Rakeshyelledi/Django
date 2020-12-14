from django.shortcuts import render,redirect
from django.http import HttpResponse
from UsApp.forms import UsReg,Updf,Imp
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Djprjct import settings
from django.core.mail import send_mail
from django.contrib import messages
from UsApp.models import ImPfle

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
			messages.success(request,'User registered successfully')
			return redirect('/login')
	t = UsReg()
	return render(request,'html/register.html',{'y':t})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def mailsend(request):
	pq = User.objects.values_list("email",flat=True)
	if request.method == "POST":
		# rec = request.POST["sndml"].split(",")
		rec = []
		adml = request.user.email
		rs = list(filter(None,pq))
		for m in rs:
			if m=="" or m==adml:
				continue
			else:
				rec.append(m)
		#print(rec)
		sub = request.POST["subject"]
		msg = request.POST["messg"]
		sd = settings.EMAIL_HOST_USER
		t = send_mail(sub,msg,sd,rec)
		if t == 1:
			messages.success(request,'{} Mail sended successfully'.format(request.user.username))
			return redirect("/mail")
		return HttpResponse("Didnt send mail to particular person")
	return render(request,'html/mailsending.html')

@login_required
def profi(request):
	return render(request,'html/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p = Updf(request.POST,instance=request.user)
		k = Imp(request.POST,request.FILES,instance=request.user.impfle)
		print(k)
		if p.is_valid() and k.is_valid():
			p.save()
			k.save()
			messages.success(request,'{} profile updated successfully'.format(request.user.username))
			return redirect('/profile')
	p = Updf(instance=request.user)
	y = Imp(instance=request.user.impfle)
	return render(request,'html/updateprofile.html',{'h':p,'q':y})