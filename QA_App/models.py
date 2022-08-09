from enum import auto
from django.db import models

# Create your models here.

class user_model(models.Model):
    auto_user_id = models.AutoField(primary_key= True)    
    full_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20,null=True)
    date_of_birth = models.DateField(null = True)
    contact_number = models.CharField(max_length=10,null=True)
    about = models.TextField(null=True)
    company_name = models.CharField(max_length=30, null=True)
    designation = models.CharField(max_length=50, null=True)
    rating_name= models.CharField(max_length=30, null=True)


    def __str__(self):
        return str(self.auto_user_id) + ',' + str(self.full_name)


class question_model(models.Model):
    auto_question_id = models.AutoField(primary_key= True)
    question_title = models.CharField(max_length=100)
    question_description = models.TextField()
    technology_name = models.CharField (max_length=20)
    status_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)    
    user_question = models.ManyToManyField(user_model)
    

    class Meta:
        ordering = ('auto_question_id',)

    def get_questions(self):
        return ",".join([str(u) for u in self.user_question.all()])

    def __str__(self):
        return str(self.auto_question_id) + ',' + str(self.question_title)

class answer_model(models.Model):
    auto_answer_id = models.AutoField(primary_key= True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    like_and_dislike = models.IntegerField(null=True)
    technology_name = models.CharField (max_length=20)
    status_name = models.CharField(max_length=20)
    user_answer = models.ForeignKey(user_model, on_delete=models.CASCADE)
    questions_answers = models.ManyToManyField(question_model)
        

    class Meta:
        ordering = ('auto_answer_id',)     

    def get_answers(self):
        return ",".join([str(q) for q in self.questions_answers.all()])


    def __str__(self):
        return str(self.auto_answer_id)


