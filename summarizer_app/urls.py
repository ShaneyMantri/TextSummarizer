from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers  # Responsible fr generating urls for models
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register('images', views.ImageView)
router.register('user', views.UserView)


urlpatterns = [
    path('', views.home, name="SummarizerHome"),
    path('api/', include(router.urls)),
    path('text_summarize', views.textSummarizer, name="TextSummarizer"),
    path('photo_summarizer', views.photoSummarizer, name="PhotoSummarizer"),
    path('register_user', views.register_user, name="APIRegister"),
    path('login_api', views.verify_login, name="APILogin"),
    path('image_upload_api', views.image_upload_api, name="ImageUploadAPI"),
    path('text_upload_api', views.text_upload_api, name="TextUploadAPI"),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]



