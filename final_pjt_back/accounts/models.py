from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # username
    username = models.CharField(max_length=30, unique=True)
    # nickname
    nickname = models.CharField(max_length=255, blank=True, null=True)
    # email
    email = models.EmailField(max_length=254, blank=True, null=True)
    # age
    age = models.IntegerField(blank=True, null=True)
    # wealth
    wealth = models.IntegerField(blank=True, null=True)
    # salary
    salary = models.IntegerField(blank=True, null=True)
    # financial_products
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username + ':' + self.nickname

    

