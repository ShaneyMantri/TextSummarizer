from django.db import models
from PIL import Image
from user.models import UserProfileInfo


class image_received(models.Model):
    username = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos_to_summarize')
    dateTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Image by {}'.format(self.username)


