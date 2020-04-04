
from django.shortcuts import render
from .models import languages, image_received, Programmer, Paradigm
from .serializers import LanguageSerializer, ImageReceivedSerializer, ParadigmSerializer, ProgrammerSerializer
from rest_framework import viewsets, permissions
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "summarizer_app/index.html")

@login_required
def textSummarizer(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        email = request.POST.get("Email")
        text_to_summarize = request.POST.get("TextToSummarize")
        """
        
        ADD SUMMARIZER CODE HERE
        
        
        """
        print("HELLO")
        print(username, email, text_to_summarize)
        context ={
                "Summarised":"Sample summarized text in hard code part 2"

        }
        print(context)
        return render(request, "summarizer_app/textsummarizer.html", {"context":context})
    return render(request, "summarizer_app/textsummarizer.html", {})



@login_required
def photoSummarizer(request):
    return render(request, "summarizer_app/photosummarizer.html", {})

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
