from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import json


# Create your views here.
# 멤버 생성(완)
# @api_view(['POST'])
# def create_member(request, pk):
#     try:
#         data_object = json.load(request)
#         name = data_object['name']
#         image = data_object['image']
#         member_id = Member.objects.filter(group__pk = pk).count() + 1
#         group = Group.objects.get(pk = pk)
#         member = Member(name = name, image = image, member_id = member_id, group = group)
#         member.save()

#         return Response(status=status.HTTP_201_CREATED)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
        

# 멤버 수정 (완)
# @api_view(['PUT'])
# def update_member(request, pk, member_id):
#     request_object = json.load(request)
    
#     try:
#         member = Member.objects.get(group__pk = pk, member_id = member_id)
#         member.name = request_object['name']
#         member.image = request_object['image']
#         member.save()
#         return Response(status=status.HTTP_200_OK)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

    

# 멤버 삭제 (완)
# @api_view(['DELETE'])
# def delete_member(request, pk, member_id):
#     member = Member.objects.get(group__pk = pk, member_id = member_id)
#     member.delete()
#     return Response(status=status.HTTP_200_OK)

# 현재 모든 멤버 확인
@api_view(['GET'])
def all_member(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many = True, context = {'request':request})
    return Response(serializer.data)

# 유저 정보 불러오기 (완)
@api_view(['GET'])
def get_member(request, group_pk, member_pk):
    user = Member.objects.get(pk = member_pk)
    group = Group.objects.get(pk = group_pk)
    member_serializer = MemberWithIDSerializer(user, context = {'request':request})
    color_serializer = GroupColorSerializer(group)
    res = member_serializer.data|color_serializer.data
    return Response(res)


# 가족 내 멤버 불러오기 (완)
@api_view(['GET'])
def get_members(request, group_pk):
    group = Group.objects.get(pk = group_pk)
    members = Member.objects.filter(group__pk = group_pk)
    members_serializer = MemberWithIDSerializer(members, many = True, context = {'request':request})
    color_serializer = GroupColorSerializer(group)
    family = members_serializer.data

    data = {}
    data['color'] = color_serializer.data['color']
    data['family'] = family
    return Response(data)
