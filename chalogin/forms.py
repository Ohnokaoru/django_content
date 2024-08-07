from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class ChaLoginForm(AuthenticationForm):
    captcha = CaptchaField()
