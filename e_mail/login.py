from e_mail import models
import logging

def login(user,pwd):
    _isExist = models.User.objects.filter(username=user,password=pwd)
    logging.warning(_isExist)
    return _isExist.exists()