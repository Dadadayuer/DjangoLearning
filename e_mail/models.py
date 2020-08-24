from django.db import models

# Create your models here.

class User(models.Model):
    username = models.EmailField(blank=False)
    create_date = models.DateTimeField('创建日期')
    is_del=models.IntegerField(default=0)
    frozen=models.IntegerField(default=0)
    password = models.CharField(max_length=60,blank=False)


class Inbox(models.Model):
    sender = models.CharField(max_length=100)
    receive_date = models.DateTimeField('创建日期')
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=256)
    attachment = models.FilePathField(default='')
    is_del = models.IntegerField(default=0)


class Drafts(models.Model):
    to = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=256)
    create_date =models.DateTimeField('创建日期')
    attachment = models.FilePathField(default='')
    is_del = models.IntegerField(default=0)


class Outbox(models.Model):
    to = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=256)
    create_date =models.DateTimeField('创建日期')
    attachment = models.FilePathField(default='')
    is_del = models.IntegerField(default=0)