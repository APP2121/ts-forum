"""QA_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.urls import path, include
from accounts import views
from django.urls import re_path as url

urlpatterns = [
        path('', views.base_view, name='home'),   
        path('profile_edit/', views.profile_edit_view, name='edit_profile'),  
        path('view_profile/',views.view_profile, name='view_profile'),
           
        path('all_questions/', views.all_questions, name = 'all_questions'),
        path('show_detailed_view_of_question/<int:pk>/', views.detailed_view_of_individual_question, name = 'detail_view'),
        path('show_answers/<int:pk>/', views.all_answers, name = 'show_answers'),
        path('show_searched_value', views.searched_vlaue, name='search_values'),
        path('answer_like_value/<int:pk>/', views.answer_like_view , name='like_value_ans'),
        path('question_like_value/<int:pk>', views.question_like_view, name='like_value_qus'),
        path('ask_question/', views.ask_question, name='ask_question'),
        path('provide_your_answer/<int:pk>/', views.provide_your_answer, name='provide_your_answer'),
        path('accounts/', include('allauth.urls')),
        path('online_compiler', views.online_compiler, name='compiler'),
        path('runcode', views.runcode, name='runcode'),        
]
