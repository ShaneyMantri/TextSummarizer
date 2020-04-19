from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from py_scirpts import summarise
from py_scirpts import image_to_text
from .forms import ImageReceivedForm
from .models import image_received
from .serializers import ImageReceivedSerializer, UserSerializer, UserLoginSerializer


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
            # summarised_text = "Sample summarised text"
            summarised_text = image_to_text.read_image(image_saved)
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



@api_view(['POST'])
def verify_login(request):

    """ CAN USE SERIAIZER FOR INITIAL_DATA"""
    # requested_user = serializer.initial_data
    # serializer = UserLoginSerializer(data=request.data)



    """ CAN ALSO USER REQUEST.DATA FOR DATA"""
    requested_user = request.data
    requested_user_dict = dict(requested_user)
    current_user = authenticate(username=requested_user_dict['username'], password=requested_user_dict['password'])
    user_pk = User.objects.get(username=requested_user_dict['username'])
    # print(requested_user_dict['password'])
    # print(str(current_user.password))
    if current_user:
        if current_user.is_active:

            return Response(requested_user, status.HTTP_200_OK)
        else:
            return Response(requested_user, status.HTTP_400_BAD_REQUEST)
    else:
        return Response(requested_user, status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def image_upload_api(request):
    image_serializer = ImageReceivedSerializer(data=request.data)
    if image_serializer.is_valid():
        image_serializer.save()
        print("Image has been uploaded")
        return Response(image_serializer.data, status.HTTP_201_CREATED)

    print("Image not uploaded")
    return Response(image_serializer.data, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def text_upload_api(request):
    data = dict(request.data)
    """
    dict = {
        "username":
        "text":
        "date-time":
    }
    """


    summarised_text = summarise.driver_fun(data['text'])
    return Response({"summarised_text":summarised_text}, status.HTTP_200_OK)


class ImageView(viewsets.ModelViewSet):
    queryset = image_received.objects.all()
    serializer_class = ImageReceivedSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer