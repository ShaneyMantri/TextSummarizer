from django.db import models
from PIL import Image


class image_received(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos_to_summarize')
    dateTime = models.DateTimeField(auto_now_add=True)



class Paradigm(models.Model):
    name=models.CharField(max_length=50)
    year = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class languages(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name= models.CharField(max_length=50)
    language = models.ManyToManyField(languages)

    def __str__(self):
        return self.name
