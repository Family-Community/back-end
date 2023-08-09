from rest_framework import serializers
from .models import CreateContent,UpdateContent

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContent
        fields = ['title', 'content', 'photo','date'] 


class UpdateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateContent
        fields = ['title', 'content', 'photo', 'date']
