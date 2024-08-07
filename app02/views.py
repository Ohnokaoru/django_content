from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# 建立基本資料
@login_required
def create_userprofile(request):
    message = ""
    form = UserProfileForm()

    # if not request.user.is_authenticated:
    #     return redirect("user-login")

    if request.method == "POST":
        form = UserProfileForm(request.POST)

        if form.is_valid():
            userprofile = form.save(commit=False)
            # 需要儲存前取得，不然與用戶關聯的資訊就會丟失，# 將當前登入用戶設置到 user 外鍵字段(手動設置user外鍵字段為 .user)
            userprofile.user = request.user
            userprofile.save()

            return redirect("userprofile-view")
        else:
            message = f"資料錯誤:"

    return render(request, "app02/create-userprofile.html", locals())


@login_required
def userprofile_view(request):
    # if not request.user.is_authenticated:
    #     return redirect("user-login")

    try:
        # 已登入一定會取到當前request.user，request.user 通常是一個 User model的實體物件，包括用戶的基本信息，如用戶名、電子郵件、密碼等
        userprofile = UserProfile.objects.get(user=request.user)

    except UserProfile.DoesNotExist:
        return redirect("create-userprofile")

    return render(request, "app02/userprofile-view.html", locals())


# 修改基本資料
@login_required
def edit_userprofile(request):
    # if not request.user.is_authenticated:
    #     return redirect("user-login")

    try:
        # request.user 通常是一個 User model的實體物件，包括用戶的基本信息，如用戶名、電子郵件、密碼等
        userprofile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect("create-userprofile")

    if request.method == "POST":
        if userprofile:
            form = UserProfileForm(request.POST, instance=userprofile)
            if form.is_valid():
                userprofile.save()

                return redirect("userprofile-view")
            else:
                message = f"資料錯誤:{form.errors}"
    else:
        form = UserProfileForm(instance=userprofile)

    return render(request, "app02/edit-userprofile.html", locals())
