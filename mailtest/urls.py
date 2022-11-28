from django.urls import path
from mailtest import views

urlpatterns = [
    path("", views.home, name="home"),
]
