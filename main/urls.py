from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ip_submit', views.ip_submit, name='ip_submit'),
]