from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder":"Enter Your Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields =['username']
		widgets = {
		"username": forms.TextInput(attrs = {"class":"form-control","placeholder": "Enter Your Username"}),
		}

class Updf(ModelForm):
	class  Meta:
		model = User
		fields = ["username","email","first_name","last_name"]
		widgets = {
		"usernamer":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name",
			}),
		}
