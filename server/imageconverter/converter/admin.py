from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import StoredImage

class ImageAdmin(ModelAdmin):
    list_display = ["id", "__unicode__", "owner" ]

admin.site.register(StoredImage, ImageAdmin)