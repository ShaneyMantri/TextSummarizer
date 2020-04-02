
from django.shortcuts import render
from .models import languages, image_received, Programmer, Paradigm
from .serializers import LanguageSerializer, ImageReceivedSerializer, ParadigmSerializer, ProgrammerSerializer
from rest_framework import viewsets, permissions

def home(request):
    return render(request, "summarizer_app/index.html")

class LanguageView(viewsets.ModelViewSet):
    queryset = languages.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ImageView(viewsets.ModelViewSet):
    queryset = image_received.objects.all()
    serializer_class = ImageReceivedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
