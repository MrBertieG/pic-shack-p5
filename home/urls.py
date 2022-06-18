from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact_us, name='contact_us'),
    path('', views.index, name='home'),
]
