from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# from argon2 import PasswordHasher

# Create your views here.

@api_view(['POST'])
def create_group(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        new_group = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_group(request, pk):
    group = Group.objects.get(pk = pk)
    group.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def entry_check(request, pk, entry_number):
    group = Group.objects.get(pk = pk)
    if group.entry_number == entry_number:
        return Response(True)
    return Response(False)

