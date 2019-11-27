

from django.conf.urls import url,include
from django.contrib import admin
import landing
from . import views
from landing.views import test
from landing.views import index

urlpatterns = [
    url('test/', views.test, name='test'),
    url('', views.index, name='index'),
     
]