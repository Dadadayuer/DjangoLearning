from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from e_mail import login as signin
from e_mail import models
import logging
import json
from e_mail import Mail

# Create your views here.

def login(request):
    if request.content_type =='multipart/form-data':
        logging.warning(request.content_type)
        username = request.POST['username']
        password = request.POST['password']
        if (username == None)|(password == None):
            return JsonResponse({
                'code': 200,
                'message': '用户名或密码不能为空！',
            })
        _checkPwd = signin.login(username,password)
        print('tpye:checkPwd',_checkPwd)
        if _checkPwd:
            return JsonResponse({
                'code': 200,
                'message': '账户验证成功！',
            })
        # return render(request,'e_mail/login.html',{
        #     'name':username,
        #     'passoword':password,
        # })
        return JsonResponse({
            'code':200,
            'message':'账户不存在！',
        })
    else:
        return JsonResponse({
            'code': 200,
            'message': '请提交multipart/form-data类型表单！',
        })

def register(request):
    _registerInfo = request.body
    userInfo = json.loads(_registerInfo.decode(encoding='utf-8'))
    username = userInfo.get('username',None)
    password = userInfo.get('password',None)
    if (username == None) | (password== None):
        return JsonResponse({
            'code':200,
            'message':'用户名或密码不能为空！',
        })
    _checkUser = signin.regiester(username)
    if _checkUser:
        return JsonResponse({
            'code':200,
            'message':'该用户名已被注册！',
        })
    models.User.objects.create(username=username,password=password,)
    return JsonResponse({
        'code':200,
        'message':'注册成功！',
    })


def bind_email_login(request):
    if request.content_type =='multipart/form-data':
        username = request.POST['username']
        password = request.POST['password']
        mailname = request.POST['mailname']
        if mailname == 'qq':
            host = Mail.Mail_host.host_imap_QQ.value
            port = Mail.Mail_port.port_imap_QQ.value
        mail =Mail.Mail()
        try:
            mail.connect(host,port)
            check_state = mail.login(username,password)
            mail.fetch_mailboxes()
        except Exception as e:
            return JsonResponse({
                'code': 200,
                'message': str(e.args[0]),
            })
        return JsonResponse({
            'code':200,
            'message':check_state,
        })
    else:
        return JsonResponse({
            'code': 200,
            'message': '请提交multipart/form-data类型表单！',
        })

def getMail(mail):




