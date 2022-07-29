from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('ppp',views.profilelist, basename='ppp')
urlpatterns = [
    #path('register', views.registerPage, name='register'),
    #path('login', views.loginPage, name='login'),
    #path('logout', views.logoutPage, name='logout'),
    path('', views.homePage, name='index'),
    path('detail',views.profile, name='profile'),
    path('view_profile',views.view_profile, name='view_profile'),
    path('get/',include(router.urls)),
    path('accounts/', include('allauth.urls')),
]