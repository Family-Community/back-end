from rest_framework import serializers
from .models import Group, Member

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['group', 'name', 'img']

class MemberPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'img']