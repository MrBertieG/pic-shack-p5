from django.urls import path
from . import views


urlpatterns = [
    path('newsletter', views.newsletter, name='newsletter'),
    path('unsubscribe', views.unsub_newsletter, name='unsub_newsletter'),
]
