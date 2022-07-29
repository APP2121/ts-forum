from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserModel(models.Model):

    
    full_name = models.CharField(max_length=20,null=True)
    date_of_birth = models.DateField(null = True)
    contact_number = models.CharField(max_length=10,null=True)
    about = models.TextField(null=True)
    company_name = models.CharField(max_length=30, null=True)
    designation = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.company_name
    
class ratingModel(models.Model):
    rating_id = models.IntegerField(null=True)
    rating_name= models.CharField(max_length=30, null=True)
    usermodel_rating= models.ForeignKey(UserModel,related_name='relation', on_delete=models.CASCADE)
