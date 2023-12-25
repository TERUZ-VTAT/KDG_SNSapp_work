from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import top

urlpatterns = [
    path('login/',LoginView.as_view(redirect_authenticated_user=True,template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),    # 追加
    path('', top, name='top')
]