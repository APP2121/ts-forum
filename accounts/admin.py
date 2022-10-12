from atexit import register
from django.contrib import admin
from .models import question_model, answer_model, User


@admin.register(User)
class userModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'nick_name', 'contact_number', 'about', 'email', 'date_of_birth', 'company_name', 'designation', 'last_login_time', 'last_logout_time', 'is_active', 'email_verified', 'is_admin', 'is_staff', 'is_superuser']
    

@admin.register(question_model)
class questionModelAdmin(admin.ModelAdmin):
    list_display = ['question_title', 'question_description', 'technology_name', 'status_name', 'created_at', 'user_questions']
            

@admin.register(answer_model)
class answerModelAdmin(admin.ModelAdmin):
    list_display = ['answer', 'created_at', 'technology_name', 'status_name', 'user_answers', 'question_answers']

