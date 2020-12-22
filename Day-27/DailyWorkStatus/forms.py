from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from DailyWorkStatus.models import Exfd,Worklog


class Usregis(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]
		widgets = {
		"first_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your First Name",
			"required":True,
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Last Name",
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Emailid",
			"required":True,
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your UserName",
			"required":True,
			}),
		}

class Upd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username": forms.TextInput(attrs={
			"class":"form-control",
			}),
		"first_name": forms.TextInput(attrs={
			"class":"form-control",
			}),
		"last_name": forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Last Name",
			}),
		"email": forms.EmailInput(attrs={
			"class":"form-control",
			}),
		}

class Pad(forms.ModelForm):
	class Meta:
		model = Exfd
		fields = ["rollno","collagename","age","gender","impfle"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			}),
		"rollno":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Roll Number",
			}),
		"collagename":forms.Select(attrs={
			"class":"form-control",
			}),
		}

class WrkForm(forms.ModelForm):
	class Meta:
		model = Worklog
		fields = ["date","description","workstatus"]
		widgets = {
		"date":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control",
			"rows":5,
			"cols":10,
			"placeholder":"Update Your Task",
			}),
		"workstatus":forms.Select(attrs={
			"class":"form-control",
			}),
		}