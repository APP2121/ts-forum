from ast import Or
from requests import post
import QA_App
from QA_App.form import answer_form, question_form
from QA_App.models import question_model, answer_model, user_model
from django.shortcuts import redirect, render
from django.db.models import Q
from rest_framework import viewsets
from QA_App.serializers import answer_serializer, question_serializer, user_serializer

class userViewSet(viewsets.ModelViewSet):
    queryset = user_model.objects.all()
    serializer_class = user_serializer

class questionViewSet(viewsets.ModelViewSet):
    queryset = question_model.objects.all()
    serializer_class = question_serializer

class answerViewSet(viewsets.ModelViewSet):
    queryset = answer_model.objects.all()
    serializer_class = answer_serializer



def base_view(request):
    ques = question_model.objects.all()
    usr = user_model.objects.all()
    return render(request, 'question_template/question_home.html', {'questions': ques, 'users': usr})

def all_questions(request):
    ques = question_model.objects.all()
    return render (request, 'question_template/view_question.html', {'questions': ques})


def detailed_view_of_individual_question(request, pk):
    ques = question_model.objects.get(auto_question_id = pk)
    return render(request, 'question_template/individual_detailed_question_template.html', {'question': ques})


def all_answers(request, pk):
    ans = answer_model.objects.filter(questions_answers = pk)
    return render(request, 'answer_template/answer_template.html', {'answers': ans})


def searched_vlaue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        detail = user_model.objects.filter(Q(auto_user_id = searched))
        return render(request, 'search_template/search_template.html', {'search': searched, 'user_detail': detail} )
    else:
        return render(request, 'search_template/search_template.html', {})


def ask_question(request):
    new_question_form = question_form()
    if request.method == 'POST':
        new_question_form = question_form(request.POST)
        if new_question_form.is_valid():
            new_question_form.save()
        return redirect(base_view)
    return render(request, 'form_template/ask_question_form.html', {'form': new_question_form} )


def provide_your_answer(request):
    new_answer_form = answer_form()
    if request.method == 'POST':
        new_answer_form = answer_form(request.POST)
        if new_answer_form.is_valid():
            new_answer_form.save()
        return redirect(base_view)
    return render(request, 'form_template/create_your_answer_form.html', {'form': new_answer_form})
    
