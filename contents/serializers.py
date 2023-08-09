from rest_framework import serializers
from .models import Content
from family.serializers import *

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class ContentUserSerializer(serializers.ModelSerializer):
    member = MemberPostSerializer()
    class Meta:
        model = Content
        fields = ['member', 'title', 'content', 'photo', 'date']


class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'content', 'photo']