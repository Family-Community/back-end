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

    # def validate_image(self, value):
    #     img = Image.open(value)
    #     width, height = img.size

    #     min_side = min(width, height)
    #     left = (width - min_side) // 2
    #     top = (height - min_side) // 2
    #     right = (width + min_side) // 2
    #     bottom = (height + min_side) // 2
    #     img = img.crop((left, top, right, bottom))

    #     target_size = (300, 300)  # 원하는 크기로 변경
    #     img.thumbnail(target_size, Image.LANCZOS)

    #     buffer = BytesIO()
    #     img.save(buffer, format='JPEG')
    #     value.file = buffer

    #     return value

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
