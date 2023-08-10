from rest_framework import serializers
from .models import *
from family.serializers import *

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'


class ReactionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['user_smile', 'user_good', 'user_sad', 'user_heart', 'user_worry', 'user_check']


class ContentSerializer(serializers.ModelSerializer):
    reaction = ReactionUserSerializer()
    class Meta:
        model = Content
        fields = ['id', 'title', 'content', 'photo', 'date', 'reaction']


class ContentUserSerializer(serializers.ModelSerializer):
    member = MemberWithIDSerializer()
    reaction = ReactionUserSerializer()
    class Meta:
        model = Content
        fields = ['member', 'title', 'content', 'photo', 'date', 'reaction']


class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'content', 'photo']


