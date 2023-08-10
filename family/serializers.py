from rest_framework import serializers
from .models import Group, Member
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['color']


class GroupPkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'family_name', 'color']


class MemberSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Member

        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None

    # def create(self, data):
    #     group = self.context.get('group')
    #     member_id = self.context.get('member_id')
    #     return Member.objects.create(group = group, member_id = member_id, **data)

class MemberCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Member
        fields = ['id', 'name', 'image']

    def validate_image(self, value):
        
        img = Image.open(value)
        max_size = (50, 50)  # 가로, 세로
        img.thumbnail(max_size, Image.LANCZOS)

        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        value.file = buffer

        return value

class MemberWithoutIDSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Member
        fields = ['name', 'image']
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None

class MemberWithIDSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Member
        fields = ['id', 'name', 'image']
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None
