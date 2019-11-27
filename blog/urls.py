from django.conf.urls import url,include
from django.contrib import admin
import landing
from . import views


urlpatterns = [
    url('', views.index, name='index'),     
]