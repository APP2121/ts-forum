from django.urls import path,include 
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("users", views.UserView, basename='user')
urlpatterns = [
    path('', views.homePage, name='index'),
    path('detail',views.profile, name='profile'),
    path('v1/', include(router.urls)),
    path('view_profile',views.view_profile, name='view_profile'),
    path('accounts/', include('allauth.urls')),
]