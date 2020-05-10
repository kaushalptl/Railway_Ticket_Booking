from django.conf.urls import url
from login_module import views
from django.urls import path,include

urlpatterns = [
 url(r'adminlogin/$', views.adminlogin),
 url(r'login/$', views.login),
 url(r'verify/$', views.verification),
 url(r'valid/$', views.valid),
 url(r'addtrain/$', views.addtrain),
 url(r'removetrainpage/$', views.removetrainpage),
 url(r'adminhome/$', views.adminhome),
 url(r'invalid/$', views.invalid),
 url(r'again/$', views.again),
 url(r'remove/$', views.remove),
 url(r'addtrainpage/$', views.addtrainpage),
 url(r'trainadded/$', views.trainadded),
 url(r'trainremoved/$', views.trainremoved),
 url(r'home/$', views.home),
 url(r'ticket/$', views.ticket),
  url(r'cost/$', views.cost),
]