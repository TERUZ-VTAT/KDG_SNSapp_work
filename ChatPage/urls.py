from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.Chat.as_view(), name="top"),
    path("<str:roomID>/", views.room, name="room"),
]
