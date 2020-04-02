from rest_framework import serializers
from .models import languages, image_received, Paradigm, Programmer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = languages
        fields = ("url","id","name","paradigm")


class ImageReceivedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = image_received
        fields = "__all__"

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = "__all__"


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = "__all__"