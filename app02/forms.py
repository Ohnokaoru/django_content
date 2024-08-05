from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    # 表單與模型關聯，並設定表單的其他屬性。
    class Meta:
        model = UserProfile
        # 全部欄位
        # fields = "__all__"

        # 選取欄位
        fields = ["customername", "gender", "birthday", "tel", "email", "address"]

        # 排除欄位
        exclude = ["user"]
