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
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView

# Create your views here.
# 멤버 생성
class CreateMember(CreateAPIView):
    serializer_class = MemberCreateSerializer

    def form_valid(self, form):
        if 'image_original' in self.request.FILES:
            form.instance.image_original = self.request.FILES['image_original']
        
        name = self.request.POST.get('name', '')
        form.instance.name = name

        if 'image_original' not in self.request.FILES:
            form.instance.image_original = None
        
        return super().form_valid(form)

    def perform_create(self, serializer):
        group_pk = self.kwargs['group_pk']
        group = Group.objects.get(pk = group_pk)
        serializer.save(group = group)
        return Response(status=status.HTTP_201_CREATED)

# 멤버 삭제
class DeleteMember(DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberWithIDSerializer

# 멤버 수정
class UpdateMember(UpdateAPIView):
    serializer_class = MemberCreateSerializer

    def put(self, request, pk, format = None):
        instance = Member.objects.get(pk = pk)

        if 'image_original' in request.data and isinstance(request.data['image_original'], str):
            self.serializer_class = MemberWithoutImageSerializer
        else:
            self.serializer_class = MemberCreateSerializer

        serializer = self.serializer_class(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
