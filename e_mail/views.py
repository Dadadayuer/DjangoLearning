from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'e_mail/login.html',{
        'name':'Dadadayuer',
    })