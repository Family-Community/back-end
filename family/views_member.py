from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.
# 멤버 생성
@api_view(['POST'])
def create_member(request, family_code):
    group = Group.objects.get(family_code = family_code)
    serializer = MemberSerializer(data = request.data, group = group)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 멤버 수정
@api_view(['PUT'])
def update_member(reqeust, family_code, member_id):
    member = Member.objects.get(group__family_code = family_code, member_id = member_id)
    serializer = MemberSerializer(member, data = reqeust.data)
    if serializer.is_valid():
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 멤버 삭제
@api_view(['DELETE'])
def delete_member(request, family_code, member_id):
    member = Member.objects.get(group__family_code = family_code, member_id = member_id)
    member.delete()
    return Response(status=status.HTTP_200_OK)



