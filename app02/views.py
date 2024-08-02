from django.shortcuts import render, redirect
from .forms import UserProfileForm


def create_userprofile(request):
    message = ""
    form = UserProfileForm()

    if request.method == "POST":
        form = UserProfileForm(request.POST)

        if form.is_vail():
            form.save()
            # return redirect(request,"app02/userprofile.html",locals())

        else:
            message = "資料錯誤"

    return render(request, "app02/create-userprofile.html", locals())
