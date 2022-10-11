from enum import auto
from pickle import FALSE
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')        

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self, email, password, **extra_fields):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=20, blank=True, null = True)
    nick_name = models.CharField(max_length=20, blank=True, null = True)
    contact_number = models.CharField(max_length=10, blank=True, null = True)
    about = models.TextField(blank=True, null = True)
    email    = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    date_of_birth = models.DateField(null = True)
    company_name = models.CharField(max_length=30, blank=True, null = True)
    designation = models.CharField(max_length=50, blank=True, null = True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    is_active       = models.BooleanField(default=True)
    email_verified  = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.full_name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

class question_model(models.Model):
    question_title = models.CharField(max_length=100)
    question_description = models.TextField(blank = True)
    technology_name = models.CharField (max_length=20, blank=True, null = True)
    status_name = models.CharField(max_length=20, blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)  
    user_questions = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'show_user')  
    question_likes = models.ManyToManyField(User, related_name="user_questions_likes", blank=True)  

    def total_que_likes(self):
        return self.question_likes.count()


    def __str__(self):
        return str(self.question_title)

class answer_model(models.Model):
    answer = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)    
    technology_name = models.CharField (max_length=20, blank=True, null = True)
    status_name = models.CharField(max_length=20, blank=True, null = True)    
    user_answers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='show_user_answer')
    question_answers = models.ForeignKey(question_model, on_delete=models.CASCADE, related_name='show_question_answer')      
    answer_likes = models.ManyToManyField(User, related_name="user_answers_likes", blank=True)

    def total_ans_likes(self):
        return self.answer_likes.count()

    def __str__(self):
        return str(self.answer)

