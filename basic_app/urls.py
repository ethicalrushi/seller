from django.contrib import admin
from django.conf.urls import include
from . import views
from django.conf.urls import url


app_name = 'basic_app'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	

]
