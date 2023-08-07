from rest_framework import serializers
from .models import CreateContent

class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContent
        fields = '__all__' 
