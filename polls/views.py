from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404

def index(resquest):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template=loader.get_template("polls/index.html")
    context = {
        'latest_question_list':latest_question_list
    }
    return render(resquest,'polls/index.html',context)

def detail(request,question_id):
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request,'polls/detail.html')
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response="正在查看问卷%s的结果。"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse('请为问卷%s提交您的答案' % question_id)