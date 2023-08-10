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
    class Meta:
        model = Member

        fields = '__all__'

    # def create(self, data):
    #     group = self.context.get('group')
    #     member_id = self.context.get('member_id')
    #     return Member.objects.create(group = group, member_id = member_id, **data)

class MemberPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'image']


class MemberCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'image']