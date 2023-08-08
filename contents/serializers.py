from rest_framework import serializers
from .models import CreateContent

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContent
        fields = ['title', 'content', 'photo','date'] 
