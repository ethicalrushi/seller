from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'Loginapp'

urlpatterns = [
	url(r'^login/', views.user_login , name='user_login' ),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.user_logout, name='user_logout'),

]

