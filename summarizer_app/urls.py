from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers  # Responsible fr generating urls for models
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('images', views.ImageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)


urlpatterns = [
    path('', views.home, name="SummarizerHome"),
    path('api/', include(router.urls)),
    path('text_summarize', views.textSummarizer, name="TextSummarizer"),
    path('photo_summarizer', views.photoSummarizer, name="PhotoSummarizer"),
    path('success', views.success, name='success')



]
