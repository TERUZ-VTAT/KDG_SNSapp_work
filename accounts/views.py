from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm, MailResetForm, iconForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import iconPath
from django.conf import settings
import os

# Create your views here.


@login_required
def top(request):
    # ユーザーモデルを取得する
    user = get_user_model()
    # ユーザーをすべて取得する
    users = user.objects.all()
    userID = request.user.id
    icon = iconPath.objects.all().filter(userid__exact=userID)
    print(icon)
    # ユーザー一覧をコンテキスト情報に入れる
    for c in icon:
        # os.remove(f"{settings.MEDIA_ROOT}/{c.filepath}")
        print(f"{settings.MEDIA_ROOT}/{c.filepath}")
    if request.POST:
        form = iconForm(request.POST, request.FILES)
        if form.is_valid():
            if icon == None:
                form.save()
            else:
                #
                for c in icon:
                    try:
                        os.remove(f"{settings.MEDIA_ROOT}/{c.filepath}")
                    except Exception:
                        pass
                    # print(f"{settings.MEDIA_ROOT}/{c.filepath}")
                    c.delete()
                form.save()

        # new_icon = request.POST['imgFile']
        # print(new_icon)
    else:
        form = iconForm()
    context = {'users': users, 'icon': icon, 'form': form}
    # top.htmlをレンダリング
    return render(request, 'top.html', context)


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:top')

    def form_valid(self, form):
        user = form.save()  # formの情報を保存
        login(self.request, user)  # 認証
        self.object = user
        return HttpResponseRedirect(self.get_success_url())  # リダイレクト


def ChangeMail(request):
    form = MailResetForm()
    if request.POST:
        userid = request.POST['userid']
        hashedPass = request.POST['hashedPass']
        password = request.POST['password']
        email = request.POST['new_mail']
        if check_password(password, hashedPass):
            user = User.objects.get(id=userid)
            user.email = email
            user.save()

    return render(request, 'mailadressReset.html', {'form': form, })
