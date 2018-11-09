from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class AppUser(AbstractUser):
    """アプリで利用するユーザー"""

    # 画像保存先指定./media/profilesになる
    profile_picture = models.ImageField(upload_to='profiles')
    
    objects = UserManager()
    
    def __str__(self):
        return self.username


class Customer(models.Model):
    """顧客"""

    name = models.CharField('顧客名', max_length=255)
    rank = models.CharField('ランク', max_length=1)
    user = models.ForeignKey(AppUser, verbose_name='担当者', related_name='customers', on_delete=models.PROTECT)

    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """製品"""

    customer = models.ForeignKey(Customer, verbose_name='顧客', related_name='products', null=True, on_delete=models.SET_NULL)
    name = models.CharField('製品名', max_length=255)
    unit_price = models.IntegerField('単価', default=0)
    unit = models.CharField('単位', max_length=10)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name
