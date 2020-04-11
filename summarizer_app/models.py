from django.db import models
from PIL import Image


class image_received(models.Model):
    username = models.CharField(max_length=100, default="")
    # image = models.FileField(upload_to='photos_to_summarize', null=True, blank=True)
    image = models.FileField(upload_to='photos_to_summarize', null=True, blank=True)
    dateTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Image by {}'.format(self.username)


