from django.http import HttpResponse
from django.template import loader
from DjangoFramework.models import Question
from django.shortcuts import render

def index(request):
    import sqlite3
    # conn =sqlite3.connect('DjangoFramework.db')
    # conn.close()
    # return HttpResponse('Hello world! You are at the polls index.')
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    template =loader.get_template('DjangoFramework/index.html')
    context={
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def details(request,question_id):
    # return HttpResponse('You are looking at question %s.' %question_id)
    context={
        'id':question_id,
    }
    return render(request,'DjangoFramework/detail.html',context=context)

def results(request, question_id):
    response ='You are looking at the result of question %s'
    return HttpResponse(response%question_id)


def vote(request,question_id):
    return HttpResponse('You are voting on question %s'%question_id)



