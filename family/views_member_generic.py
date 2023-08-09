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
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
# 멤버 생성
class CreateMember(CreateAPIView):
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        group_pk = self.kwargs['group_pk']
        group = Group.objects.get(pk = group_pk)
        serializer.save(group = group)
        return Response(status=status.HTTP_201_CREATED)


class MemberDetail(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberPostSerializer
