
from django.shortcuts import render, redirect
from .models import CreateContent
from django.views.decorators.http import require_POST
from rest_framework.response import Response
from rest_framework import status


@require_POST #post만 수행
def upload_content(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    photo_url = request.POST.get('photo')

    return Response(status=status.HTTP_201_CREATED)
