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

# 게시글 작성
@api_view(['POST'])
def create_post(request):
    return Response(status=status.HTTP_201_CREATED)


# 게시글 수정
@api_view(['PUT'])
def update_post(request):
    return Response(status=status.HTTP_200_OK)


# 게시글 삭제
@api_view(['DELETE'])
def delete_post(request):
    return Response(status=status.HTTP_200_OK)

# 리액션 작성
@api_view(['PUT'])
def reaction(request):
    return Response(status=status.HTTP_200_OK)
