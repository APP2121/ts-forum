from ast import Or
from multiprocessing import context
from time import time
from requests import post
import accounts
from accounts import forms
from accounts.forms import answer_form, question_form, user_model_form, userProfile_form
from accounts.models import question_model, answer_model, User
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from accounts.serializers import answer_serializer, question_serializer, user_serializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login, logout
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from accounts.forms import user_model_form, userProfile_form, answer_form, question_form  
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
import sys

from difflib import get_close_matches

def closeMatches(patterns, word):
    print(get_close_matches(word, patterns))



from django.contrib.auth import get_user_model
User = get_user_model()

class questionViewSet(viewsets.ModelViewSet):
    queryset = question_model.objects.all()
    serializer_class = question_serializer

class answerViewSet(viewsets.ModelViewSet):
    queryset = answer_model.objects.all()
    serializer_class = answer_serializer

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer
    permission_classes = [AllowAny]

def profile_edit_view(request):
    form = user_model_form()
    if request.method == 'POST':        
        pro = user_model_form(request.POST,instance=request.user)        
        if pro.is_valid():
            pro.save()
            messages.success(request, 'Profile is created.')
        return redirect(base_view)    
    return render(request, 'allauth/detail.html', {'form' :  form})

def view_profile(request):
    profile = request.user 
    return render(request, 'allauth/view_profile.html', {'profile':profile})


def base_view(request):
    count = User.objects.count()
    ques = question_model.objects.all()
    usr = User.objects.all()
    return render(request, 'question_template/question_home.html', {'questions': ques, 'users': usr, 'count': count})


def all_questions(request):
    ques = question_model.objects.all()
    return render (request, 'question_template/view_question.html', {'questions': ques})

def detailed_view_of_individual_question(request, pk):
    
    ques = question_model.objects.get(id = pk)
    ans = answer_model.objects.filter(question_answers = pk) 

    current_question_title = ques.question_title
    list_of_questionTags = []
    list_of_similarQuestions = []

    list_of_questions = question_model.objects.all()
    for question in list_of_questions:
        list_of_questionTags.append(question.question_title)

    list_of_similarQuestions = get_close_matches(current_question_title, list_of_questionTags)
    final_list_of_similar_questions = [i for i in list_of_similarQuestions if i != current_question_title]

    combined_pair_for_suggested_que_and_ans = []
    for que in final_list_of_similar_questions:
        searched_question = question_model.objects.get(question_title = que)
        searched_ans = answer_model.objects.filter(question_answers = searched_question.id)
        combined_pair_for_suggested_que_and_ans.append([que, searched_ans])

    new_answer_form = answer_form()
    if request.method == 'POST':
        
        new_answer_form = answer_form(request.POST)
        if new_answer_form.is_valid():            
            answer1 = new_answer_form.save(commit=False)
            answer1.created_at = timezone.now()
            answer1.technology_name = ques.technology_name
            answer1.status_name = ques.status_name
            answer1.user_answers = request.user
            answer1.question_answers = ques            
            answer1.save()
            messages.success(request,'Answer has been submited.')
        return HttpResponseRedirect(reverse('detail_view', args=[str(pk)]))

    return render(request, 'question_template/individual_detailed_question_template.html', {'question': ques, 'answers': ans, 'form': new_answer_form, 'similar_questions_answers_combined_pair': combined_pair_for_suggested_que_and_ans})


def all_answers(request, pk):
    ans = answer_model.objects.filter(question_answers = pk)
    return render(request, 'answer_template/answer_template.html', {'answers': ans})


def searched_vlaue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        detail = User.objects.filter(Q(id = searched))
        return render(request, 'search_template/search_template.html', {'search': searched, 'user_detail': detail} )
    else:
        return render(request, 'search_template/search_template.html', {})

@login_required
def answer_like_view(request, pk):   
    likes = get_object_or_404(answer_model, id= request.POST.get('answer.id')) 
    liked = False
    if likes.answer_likes.filter(id= request.user.id).exists():
        likes.answer_likes.remove(request.user)
        liked = False
    else:
        likes.answer_likes.add(request.user)
        liked = True
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    

@login_required
def question_like_view(request, pk):
    likes = get_object_or_404(question_model, id= request.POST.get('question.id'))
    liked = False
    if likes.question_likes.filter(id = request.user.id).exists():
        likes.question_likes.remove(request.user)
        liked = False
    else:
        likes.question_likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_view', args=[str(pk)]))    


@login_required
def ask_question(request):
    new_question_form =forms.question_form()
    if request.method == 'POST':
        new_question_form = forms.question_form(request.POST)         
        if new_question_form.is_valid():            
            question1 = new_question_form.save(commit=False)
            question1.question_title = new_question_form.cleaned_data.get("question_title")
            question1.question_description = new_question_form.cleaned_data.get("question_description")
            question1.technology_name = new_question_form.cleaned_data.get("technology_name")
            question1.status_name = new_question_form.cleaned_data.get("status_name")              
            question1.user_questions = request.user
            question1.save()
        return redirect(base_view)
    return render(request, 'form_template/ask_question_form.html', {'form': new_question_form} )


@login_required
def provide_your_answer(request, pk):        
    new_answer_form = answer_form()
    quest = question_model.objects.get(id = pk)
    if request.method == 'POST':        
        new_answer_form = answer_form(request.POST)
        if new_answer_form.is_valid():            
            answer1 = new_answer_form.save(commit=False)
            answer1.created_at = timezone.now()
            answer1.technology_name = quest.technology_name
            answer1.status_name = quest.status_name
            answer1.user_answers = request.user
            answer1.question_answers = quest            
            answer1.save()
        return redirect(base_view)
    return render(request, 'form_template/create_your_answer_form.html', {'form': new_answer_form})

def online_compiler(request):
    return render(request, 'online_compiler/online_compiler.html')

def runcode(request):
    if request.method == "POST":
        code_area = request.POST['codearea']
        
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_area)            
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout
            output = e
    return render(request, 'online_compiler/online_compiler.html', {"code": code_area, "output": output})
