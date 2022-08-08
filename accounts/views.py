from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import  User
from .forms import UserForm, RegisterUserForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import viewsets
from . serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def get_instance(self):
        return self.request.user

    def user_profile(self, request, pk):
        obj = self.get_object()
        serializer = self.UserSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return render(request, 'register1.html')


def profile(request):
    form = RegisterUserForm()
    print(1)
    if request.method == 'POST':
        
        pro = RegisterUserForm(request.POST,instance=request.user)
        
        if pro.is_valid():
            pro.save()
            return redirect('index')
           

    context = {
        'form': form
    }
    return render(request, 'detail.html', context)

def view_profile(request):
    profile = request.user 
    return render(request, 'View_profile.html', {'profile':profile})

def homePage(request):
    User1 = User.objects.all()
    return render(request, 'homepage.html')

