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
def create_member(request, pk):
    group = Group.objects.get(pk = pk)
    member_id = Member.objects.filter(group=group).count() + 1
    img = request.FILES
    serializer = MemberSerializer(data=request.data, img = img, context={'group': group, 'member_id': member_id})
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 멤버 수정
@api_view(['PUT'])
def update_member(request, pk, member_id):
    member = Member.objects.get(group__pk = pk, member_id = member_id)
    serializer = MemberSerializer(member, data = request.data)
    if serializer.is_valid():
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 멤버 삭제
@api_view(['DELETE'])
def delete_member(request, pk, member_id):
    member = Member.objects.get(group__pk = pk, member_id = member_id)
    member.delete()
    return Response(status=status.HTTP_200_OK)

# 현재 모든 멤버 확인
@api_view(['GET'])
def all_member(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many = True)
    return Response(serializer.data)