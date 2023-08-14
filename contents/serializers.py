from rest_framework import serializers
from .models import *
from family.serializers import *


# 개발자 확인용 시리얼라이저
# 게시글을 작성한 유저에 대한 정보는 없음
class ContentSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None
    
    class Meta:
        model = Content
        fields = '__all__'
        # fields = [
            # 'id',
            # 'title',
            # 'content',
            # 'photo',
            # 'date',
            # 'user_smile',
            # 'user_good',
            # 'user_sad',
            # 'user_heart',
            # 'user_worry',
            # 'user_check'
        # ]

    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url)
        return None


# 유저에게 보여지는 데이터의 시리얼라이저
class ContentUserSerializer(serializers.ModelSerializer):
    member = MemberWithIDSerializer()
    photo = serializers.SerializerMethodField()
    
    class Meta:
        model = Content
        fields = '__all__'

    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.photo.url)
        return None


# 게시글 작성 시의 시리얼라이저
class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'content', 'photo']
