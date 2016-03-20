from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice


# Create your views here.
def index(request):
    listOfQuestions = Question.objects.all()[:5]
    #output = '<b>'
    #for i in range(0, len(listOfQuestions)):
    #    output = output + listOfQuestions[i].question_text
    #    output = output + ', '
    #output = output + '</b>'
    template = loader.get_template('firstApp/index.html')
    context = {
        'listOfQuestions': listOfQuestions,
    }
    return HttpResponse(template.render(context, request))

def testJoe(request):
    return HttpResponse("ya ya ya ya ")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
