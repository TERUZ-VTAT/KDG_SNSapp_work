from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import top, SignUp

urlpatterns = [
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),    # 追加
    path('signup/', SignUp.as_view(), name='signup'),
    path('', top, name='top')
]