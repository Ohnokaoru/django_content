from django.shortcuts import render, redirect
from .forms import ChaLoginForm
from django.contrib.auth import login


# Create your views here.
def user_chalogin(request):
    form = ChaLoginForm()
    if request.method == "POST":
        form = ChaLoginForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")

    return render(request, "chalogin/user-chalogin.html", locals())
