from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from e_mail import login as signin

# Create your views here.

def login(request):
    username = request.POST['username']
    password = request.POST['password']
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

