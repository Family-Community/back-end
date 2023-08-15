from rest_framework import serializers
from .models import *
from family.serializers import *

# class ReactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reaction
#         fields = '__all__'


# class ReactionUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reaction
#         fields = ['user_smile', 'user_good', 'user_sad', 'user_heart', 'user_worry', 'user_check']


class ContentSerializer(serializers.ModelSerializer):
    # reaction = ReactionUserSerializer()
    photo = serializers.SerializerMethodField()
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None
    
    class Meta:
        model = Content
        fields = '__all__'
        # fields = ['id', 'title', 'content', 'photo', 'date', 'user_smile', 'user_good', 'user_sad', 'user_heart', 'user_worry', 'user_check'] # 'reaction'

    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url)
        return None


class ContentUserSerializer(serializers.ModelSerializer):
    member = MemberWithIDSerializer()
    photo = serializers.SerializerMethodField()
    # reaction = ReactionUserSerializer()
    
    class Meta:
        model = Content
        fields = '__all__'
        # fields = ['member', 'title', 'content', 'photo', 'date', 'user_smile', 'user_good', 'user_sad', 'user_heart', 'user_worry', 'user_check'] # 'reaction'


    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url)
        return None


class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'content', 'photo']


class GetContentSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    
    class Meta:
        model = Content
        fields = ['title', 'content', 'photo']

    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url)
        return None