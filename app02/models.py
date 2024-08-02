from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    customername = models.CharField(max_length=20)
    GENDER_CHOICES = [("M", "男"), ("F", "女")]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    # user是id
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 後台的顯示欄位
    def __str__(self):
        return f"{self.user} {self.customername}"
