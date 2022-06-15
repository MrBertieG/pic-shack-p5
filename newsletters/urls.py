from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/newsletters/', views.newsletter_signup, name='newsletters_signup'),
    path('unsubscribe/newsletters/', views.newsletter_unsubscribe, name='newsletters_unsubscribe'),
]
