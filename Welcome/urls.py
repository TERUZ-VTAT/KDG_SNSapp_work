from django.urls import path
from . import views

urlpatterns = [
    path("", views.firstPage),
    path("welcome/", views.Welcome.as_view(), name="welcome")
]
