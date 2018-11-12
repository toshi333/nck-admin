from django.db import models
from datetime import datetime
from django.contrib.auth.models import Group
from master.models import AppUser, Customer, TaskCd


class Project(models.Model):
    """案件"""

    PROJECT_TYPE_CHOICES = ((1, '一括'), (2, '派遣'), (3, '保守'), (9, 'その他'))
    PROJECT_STATUS_CHOICES = ((1, 'プレ'), (2, '受注'), (3, '売上'), (9, '終番'))

    project = models.CharField('作番', primary_key=True, max_length=7)
    title = models.CharField('案件名', max_length=255)
    type = models.IntegerField('分類', choices=PROJECT_TYPE_CHOICES, default=1)
    status = models.IntegerField('状態', choices=PROJECT_STATUS_CHOICES, default=1)
    customer = models.ForeignKey(Customer, verbose_name='顧客名', on_delete=models.PROTECT)
    group = models.ForeignKey(Group, verbose_name='集計部門', on_delete=models.PROTECT)
    owner = models.ForeignKey(AppUser, verbose_name='案件担当者', on_delete=models.PROTECT, related_name='projects')
    members = models.ManyToManyField(AppUser, verbose_name='案件メンバー', blank=True, related_name='member_projects')
    topic = models.CharField('要点', blank=True, null=True, max_length=400)

    start_date = models.DateField('作番開始日', default=datetime.now)
    end_date = models.DateField('作番終了日')
    expected_order_date = models.DateField('受注予定日', blank=True, null=True)
    order_date = models.DateField('受注日', blank=True, null=True)
    expected_sales_date = models.DateField('売上予定日', blank=True, null=True)
    sales_date = models.DateField('売上日', blank=True, null=True)
    expected_price = models.IntegerField('予想金額', default=0)
    order_price = models.IntegerField('受注金額', blank=True, null=True)
    sales_price = models.IntegerField('売上金額', blank=True, null=True)

    created_at = models.DateTimeField('登録日時', default=datetime.now)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        # DBテーブル名
        db_table = 'project'

    def __str__(self):
        return self.title


class ProjectTask(models.Model):
    """案件作業"""
    project = models.ForeignKey(Project, verbose_name='作番', on_delete=models.CASCADE)
    task = models.ForeignKey(TaskCd, verbose_name='作業コード', blank=False, null=True, on_delete=models.SET_NULL, related_name='project_task')
    title = models.CharField('作業名', max_length=40)
    user = models.ForeignKey(AppUser, verbose_name='担当者', blank=True, null=True, on_delete=models.SET_NULL)
    man_hour = models.IntegerField('工数', default=0)
    price = models.IntegerField('金額', default=0)
    comment = models.CharField('備考', blank=True, null=True, max_length=100)

    def __inint__(self):
        self.cost = self.man_hour * 3500
        self.profit = self.price - self.cost
        self.profit_rate = self.profit / self.price

    def __str__(self):
        return self.title

    class Meta:
        # DBテーブル名
        db_table = 'project_task'
    

class ProjectRecord(models.Model):
    """作業実績"""
    user = models.ForeignKey(AppUser, verbose_name='社員', on_delete=models.PROTECT)
    work_date = models.DateField('作業日', default=datetime.now)
    project = models.ForeignKey(Project, verbose_name='作番', on_delete=models.PROTECT)
    task = models.ForeignKey(TaskCd, verbose_name='作業コード', blank=False, null=True, on_delete=models.SET_NULL)
    work_hour = models.IntegerField('作業時間', default=0)
    comment = models.CharField('備考', blank=True, null=True, max_length=100)

    def __str__(self):
        return self.user

    class Meta:
        # DBテーブル名
        db_table = 'project_record'