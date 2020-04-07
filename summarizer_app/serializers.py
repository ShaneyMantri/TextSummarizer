from rest_framework import serializers
from .models import  image_received



class ImageReceivedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = image_received
        fields = "__all__"

