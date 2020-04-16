from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from py_scirpts import summarise
# from py_scirpts import image_to_text
from .forms import ImageReceivedForm
from .models import image_received
from .serializers import ImageReceivedSerializer, UserSerializer


@login_required
def home(request):
    return render(request, "summarizer_app/index.html")

@login_required
def textSummarizer(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        email = request.POST.get("Email")
        text_to_summarize = request.POST.get("TextToSummarize")
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
            image.username = User.objects.filter(username=request.user).first()
            form.save()
            image_saved = form.cleaned_data['image']
            summarised_text = "Sample summarised text"
            # summarised_text = image_to_text.read_image(image_saved)
            print("Summarised Text", summarised_text)
            messages.error(request, f'Image Posted Successfully')
            context ={
                'summarised_text':summarised_text
            }
            return render(request, "summarizer_app/photosummarizer.html", context)

        else:
            messages.error(request, f'Invalid Form')
            return redirect('PhotoSummarizer')
    else:
        form = ImageReceivedForm()
    return render(request, "summarizer_app/photosummarizer.html", {'form': form})


@api_view(['POST'])
def register_user(request):
    serialiser = UserSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        # print("Created")
        # print(serialiser.data)
        return Response(serialiser.data, status=status.HTTP_201_CREATED)

    # print("Wrong Data")
    # print(serialiser.data)
    # print(status.HTTP_400_BAD_REQUEST)
    return Response(serialiser.data, status = status.HTTP_400_BAD_REQUEST)





class ImageView(viewsets.ModelViewSet):
    queryset = image_received.objects.all()
    serializer_class = ImageReceivedSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer