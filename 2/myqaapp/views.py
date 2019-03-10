from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.core.exceptions import ValidationError


def index(request):
    print(request.path)
    return HttpResponse("Hello, world. You're at the polls index.")


def add_question(request):
    # questions = Question.objects.all()
    shortName = request.POST.get("shortName", "")
    text = request.POST.get("text", "")
    
    try:
        newq = Question(shortName=shortName, text=text)
        newq.clean_fields()
        newq.save() 
        return render(request,
                "message.html",
                {"msg" : "Новый вопрос добавлен успешно"})
    except ValidationError as e:
        return render(request,
                "message.html",
                {"msg" : "Некоректные данные для добавления"})
    except Exception as e:
        return render(request,
                "message.html",
                {"msg" : "Ошибка добавления. Попробуйте позже"})

def all_questions(request):
    questions = Question.objects.all()
    for q in questions:
        print(q.shortName, q.text)
    return render(request, 
        "index.html",
         {"questions":questions})

def new_question(request):
    return render(request, 
        "new_question.html")