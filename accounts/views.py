#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import UserModel
from .forms import UserModelForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import viewsets
from . serializers import UserModelSerializer
from rest_framework.response import Response
#from django.contrib.auth.models import User

def profile(request):
    if request.method == "POST":
        print("hello*********")
        #username=request.POST.get('username')
        full_name=request.POST.get('full_name')
        date_of_birth=request.POST.get('date_of_birth')
        contact_number=request.POST.get('contact_number')
        company_name=request.POST.get('company_name')
        designation=request.POST.get('designation')
        about=request.POST.get('about')
        data=UserModel(full_name=full_name,date_of_birth=date_of_birth,contact_number=contact_number,company_name=company_name,designation=designation, about=about)
        data.save()
        print("work is done")
        return redirect('index')
    return render(request, 'register1.html')

def view_profile(request):
    profile=UserModel.objects.all()
    return render(request, 'View_profile.html', {'profile': profile})

def homePage(request):
    User1 = UserModel.objects.all()
    context = {
        'questions': User1
    }
    return render(request, 'homepage.html', context)


class profilelist(viewsets.ViewSet):
    def list(self,request):
        p=UserModel.objects.all()
        ser=UserModelSerializer(p,many=True)
        return Response(ser.data)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            p=UserModel.objects.get(id=id)
            serial=UserModelSerializer(p)
            return Response(serial.data)