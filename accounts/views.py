from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm

# Create your views here.
def top(request):
    # ユーザーモデルを取得する
    user = get_user_model()
    # ユーザーをすべて取得する
    users = user.objects.all()
    # ユーザー一覧をコンテキスト情報に入れる
    context = {'users': users}
    # top.htmlをレンダリング
    return render(request, 'top.html', context)

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signup.html" 
    success_url = reverse_lazy('top')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト
    
    # def get(self,request):
    #     if request.user.is_authenticated:
    #         return redirect('/chat/')
    #     else:
    #         return render(request,"signup.html")