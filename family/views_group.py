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
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView

# from argon2 import PasswordHasher

# Create your views here.

# 가족 그룹 생성
# @api_view(['POST'])
# def create_group(request):
#     try:
#         data_object = json.load(request)
#         family_name = data_object['family_name']
#         color = data_object['color']
#         entry_number = data_object['entry_number']
#         name = data_object['name']
#         image = data_object['image']
#         group = Group(family_name = family_name, color = color, entry_number = entry_number)
#         group.save()

#         member = Member(group = group, name = name, image = image, member_id = 1)
#         member.save()
#         return Response(status=status.HTTP_201_CREATED)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# 그룹 삭제
# @api_view(['DELETE'])
# def delete_group(request, pk):
#     group = Group.objects.get(pk = pk)
#     group.delete()
#     return Response(status=status.HTTP_200_OK)

# 그룹 생성
class CreateGroup(CreateAPIView):
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save()


# 그룹 삭제
class DeleteGroup(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# entry_number 확인
@api_view(['GET'])
def entry_check(request, pk, entry_number):
    group = Group.objects.get(pk = pk)
    if group.entry_number == entry_number:
        return Response(True)
    return Response(False)


# 현재 모든 그룹 확인
@api_view(['GET'])
def all_group(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many = True)
    return Response(serializer.data)