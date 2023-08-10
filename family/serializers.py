from rest_framework import serializers
from .models import Group, Member

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
    class Meta:
        model = Member
        fields = ['id', 'name', 'image']

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
