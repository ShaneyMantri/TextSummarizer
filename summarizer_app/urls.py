from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers  # Responsible fr generating urls for models

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('images', views.ImageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)


urlpatterns = [
    path('', views.home, name="SummarizerHome"),
    path('router/', include(router.urls)),



]
