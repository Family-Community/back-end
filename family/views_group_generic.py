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
# 그룹 생성
class CreateGroup(CreateAPIView):
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save()


# 그룹 삭제 / 멤버 조회
class DeleteGroup(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    


