from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User


# 建立基本資料
def create_userprofile(request):
    message = ""

    if request.method == "POST":
        # 嘗試獲取或創建 UserProfile 實例
        userprofile = UserProfile.objects.create(user=request.user)
        form = UserProfileForm(request.POST, instance=userprofile)

        if form.is_valid():
            updated_userprofile = form.save(commit=False)
            updated_userprofile.user = request.user  # 確保 user 欄位被設置
            updated_userprofile.save()

            return redirect("view-userprofile")

        else:
            message = f"資料錯誤: {form.errors}"

    else:
        # GET 請求，顯示表單
        userprofile, created = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(instance=userprofile)

    return render(request, "app02/create-userprofile.html", locals())


# 基本資料頁面與修改
def view_userprofile(request):
    form = UserProfileForm()

    # 若按下修改
    if request.method == "POST":
        userprofile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(request.POST, instance=userprofile)

        if form.is_valid():
            form.save()

            return redirect("view-userprofile")

        else:
            message = f"修改失敗{form.errors}"

    return render(request, "app02/view-userprofile.html", locals())
