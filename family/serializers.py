from rest_framework import serializers
from .models import Group, Member

class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields = ['family_name', 'color', 'entry_number']


class MemberSerializer(serializers.Serializer):
    class Meta:
        model = Member
        fields = ['group', 'name', 'img']

class MemberPostSerializer(serializers.Serializer):
    class Meta:
        model = Member
        fields = ['name', 'img']