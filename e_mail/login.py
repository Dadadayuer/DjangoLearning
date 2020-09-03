from e_mail import models
import logging

def login(user,pwd):
    _isExist = models.User.objects.filter(username=user,password=pwd)
    return _isExist.exists()


def regiester(user):
    _isExist = models.User.objects.filter(username=user)
    return _isExist.exists()