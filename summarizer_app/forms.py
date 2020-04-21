from django import forms
from .models import image_received, text_received

class ImageReceivedForm(forms.ModelForm):
    class Meta:
        model=image_received
        fields = ('image',)



class TextReceivedForm(forms.ModelForm):

    class Meta:
        model=text_received
        fields = ('text',)