from django.contrib import admin
from .models import image_received, text_received

admin.site.register(image_received)
admin.site.register(text_received)