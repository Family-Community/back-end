
from django.shortcuts import render, redirect
from .models import CreateContent
from django.views.decorators.http import require_POST
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import CreateContentSerializer  


@require_POST #post만 수행
def upload_content(request):
    serializer = CreateContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
