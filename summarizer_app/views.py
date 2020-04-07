from django.shortcuts import render, redirect
from .models import image_received
from .serializers import ImageReceivedSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageReceivedForm
from django.http import HttpResponse
from user.models import UserProfileInfo
from py_scirpts import summarise



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
        summary = summarise.driver_fun(text_to_summarize)
        context ={
                "Summarised":summary

        }
        print(context)
        return render(request, "summarizer_app/textsummarizer.html", {"context":context})
    return render(request, "summarizer_app/textsummarizer.html", {})



@login_required
def photoSummarizer(request):

    if request.method == 'POST':
        form = ImageReceivedForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.username = UserProfileInfo.objects.filter(user=request.user).first()
            form.save()
            messages.error(request, f'Image Posted Successfully')
            return redirect("PhotoSummarizer")

        else:
            messages.error(request, f'Invalid Form')
            print("HLELLEL")
            return redirect('PhotoSummarizer')
    else:
        form = ImageReceivedForm()
    return render(request, "summarizer_app/photosummarizer.html", {'form': form})





class ImageView(viewsets.ModelViewSet):
    queryset = image_received.objects.all()
    serializer_class = ImageReceivedSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

