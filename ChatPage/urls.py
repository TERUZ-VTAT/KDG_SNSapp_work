from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "chat"

urlpatterns = [
    path("", views.Chat.as_view(), name="top"),
    path("<str:roomID>/", views.room, name="room"),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset'),
    path('admin/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
