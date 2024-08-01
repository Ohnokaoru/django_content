from django.shortcuts import render

# 內建引入form
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# 內建表單會自動驗證
def user_register(request):
    message = ""

    # 建空表單給GET方法渲染用，一般進入頁面就是GET方法
    form = UserCreationForm()

    # 按下提交表單後
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        # form是否有效，會自動驗證UserCreationForm的帳密條件，並創建
        if form.is_valid:
            form.save()

    return render(request, "app01/user-register.html", locals())
