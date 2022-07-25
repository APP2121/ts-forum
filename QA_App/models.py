from enum import auto
from django.db import models

# Create your models here.

class question_model(models.Model):
    auto_question_id = models.AutoField(primary_key= True)
    question_title =models.CharField(max_length=200)
    question_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.auto_question_id)

class answer_model(models.Model):
    auto_answer_id = models.AutoField(primary_key= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_and_dislike = models.IntegerField(null=True)
    questions_answers = models.ManyToManyField(question_model)

    def __str__(self):
        return str(self.auto_answer_id)


class status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=10)
    question_status = models.OneToOneField(question_model, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.status_id)

class technology(models.Model):
    technology_id = models.IntegerField(primary_key=True)
    technology_name = models.CharField (max_lenth = 20)
    question_technology = models.ForeignKey (question_model, related_name='question_technology', on_delete=models.CASCADE)
    answer_technology = models.ForeignKey (answer_model, related_name='answer_technology', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.technology_id)


    