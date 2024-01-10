from django.urls import path
from . import views

urlpatterns = [
    path("", views.Chat.as_view()),
    path("<str:roomID>/", views.room, name="room"),
]
