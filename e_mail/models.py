from django.db import models

# Create your models here.

class User(models.Model):
    username = models.EmailField(blank=False)
    create_date = models.DateTimeField('创建日期')
    is_del=models.IntegerField(default=0)
    frozen=models.IntegerField(default=0)
    password = models.CharField(max_length=60,blank=False)


class Index(models.Model):
    sender = models.CharField(max_length=100)
    create_date = models.DateTimeField('创建日期')
    send_date = models.DateTimeField('发送时间')
    content = models.CharField(max_length=256)
    attachment = models.FilePathField(default='')
    is_del = models.IntegerField(default=0)


class