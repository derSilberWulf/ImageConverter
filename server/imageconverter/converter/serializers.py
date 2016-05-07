from django.contrib.auth.models import User
from .models import StoredImage
from rest_framework import serializers

class StoredImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField()
    class Meta:
        model = StoredImage
        fields = ('url', 'id', 'image', 'owner')
