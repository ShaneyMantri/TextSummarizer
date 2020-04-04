from django.conf.urls import url
from . import views
from django.urls import path

from summarizer_app import views as sappviews

urlpatterns=[
    path('register/',views.register, name='Register'),
    path('login/',views.user_login, name='Login'),
    path('users/', views.index, name='Index'),
    path('special/', views.special, name='Special'),
    path('logout/', views.user_logout, name='Logout'),
]