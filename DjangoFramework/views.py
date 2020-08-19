from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from DjangoFramework.models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.urls import reverse


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'DjangoFramework/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'DjangoFramework/results.html', {'question': question})


def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        value =request.POST['choice']
        selected_choice =question.choice_set.get(pk= value)
    except(KeyError,Choice.DoesNotExist):
        return render(request,'DjangoFramework/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        url =reverse('results',args=(question.id,))
        return HttpResponseRedirect(url)

def unvote(request,questio_id):
    question = get_object_or_404(Question,pk=questio_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except Exception as ex:
        return render(request,'DjangoFramework/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes -= 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(questio_id,)))


