from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# 內建引入form
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


# 內建表單會自動驗證
def index(request):
    return render(request, "app01/index.html", locals())


# 註冊後自動login並導向建立基本資料
def user_register(request):
    # 建空表單給GET方法渲染用，一般進入頁面就是GET方法
    form = UserCreationForm()

    # 按下提交表單後
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        # form是否有效，會自動驗證UserCreationForm的帳密條件，並創建
        if form.is_valid():
            # 取得user
            user = form.save()

            login(request, user)
            return redirect("create-userprofile")

    return render(request, "app01/user-register.html", locals())


# 沒有內建表單，自己手動取值
def user_login(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 認證
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

        else:
            message = "帳密錯誤"

    return render(request, "app01/user-login.html", locals())


def user_logout(request):
    logout(request)

    return redirect("index")
