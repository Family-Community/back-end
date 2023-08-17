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
        # 파일 필드 업로드 처리
        if 'image_original' in self.request.FILES:
            form.instance.image_original = self.request.FILES['image_original']
        
        # name 필드 처리
        name = self.request.POST.get('name', '')
        form.instance.name = name
        
        # ... (다른 필드들 처리)
        
        # 데이터가 없을 경우 해당 필드를 비움 (빈 문자열 또는 null로 설정)
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
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer
