from django.shortcuts import render
from django.contrib.auth import get_user_model

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