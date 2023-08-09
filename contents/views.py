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


@api_view(['POST'])
def create_post(request):
    return Response(status=status.HTTP_201_CREATED)

