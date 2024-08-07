from django.contrib import admin
from .models import UserProfile

# Register your models here.


# 後台顯示，可依照需求寫或不寫
class UserProfileAdmin(admin.ModelAdmin):
    # 顯示欄位
    list_display = (
        "id",
        "user",
        "customername",
        "gender",
        "birthday",
        "tel",
        "email",
        "address",
    )

    # 篩選欄位
    list_filter = ("gender",)

    # 一欄位搜尋
    search_fields = (
        "user",
        "customername",
    )

    # 排序
    ordering = ("user",)


# 註冊
admin.site.register(UserProfile, UserProfileAdmin)
