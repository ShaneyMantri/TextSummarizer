from django.conf.urls import url
from . import views
from django.urls import path

from summarizer_app import views as sappviews

app_name = 'user'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]