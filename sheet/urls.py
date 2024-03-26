from django.urls import path, include
from .views import *
# from django.contrib.auth.views import LoginView, LogoutView
# from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', Category.as_view(), name='tips'),
    path("about/", about, name="about"),
    path('<slug:slug>', Tips.as_view(), name='tip'),
]

