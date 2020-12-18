from django.urls import path
from DailyWorkStatus import views
from django.contrib.auth import views as v

urlpatterns = [
	path("",views.home,name="hm"),
	path("abt/",views.about,name="ab"),
	path("cnt/",views.contact,name="ct"),
	path("rg/",views.register,name="reg"),
	path("dsh/",views.dashboard,name="dash"),
	path("lg/",v.LoginView.as_view(template_name="html/login.html"),name="logi"),
	path("lgo/",v.LogoutView.as_view(template_name="html/logout.html"),name="lgot"),
]