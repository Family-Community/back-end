from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from family.models import *
from family.serializers import *
from rest_framework.decorators import api_view
from django.db.models import Q

# 게시글 생성
class CreateContent(CreateAPIView):
    serializer_class = CreateContentSerializer
    queryset = Content.objects.all()

    def perform_create(self, serializer):
        member_pk = self.kwargs['member_pk']
        member = Member.objects.get(pk = member_pk)
        serializer.save(member = member)
        return Response(status=status.HTTP_201_CREATED)

# 게시글 수정, 삭제
class UpdateDestroyContent(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = CreateContentSerializer
    lookup_url_kwarg = 'post_id'


# 현재 모든 게시글 확인
class AllContent(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


# 해당 그룹의 전체 게시글 확인
@api_view(['GET'])
def get_contents(request, group_pk):
    group = Group.objects.get(pk = group_pk)
    contents = Content.objects.filter(member__group__pk = group_pk)
    contents_serializer = ContentUserSerializer(contents, many = True)
    color_serializer = GroupColorSerializer(group)

    data = {}
    data['color'] = color_serializer.data['color']
    data['post'] = contents_serializer.data
    return Response(data)


# 그룹 내에서 키워드를 통한 게시물 검색
@api_view(['GET'])
def search_contents(request, group_pk, search):
    group = Group.objects.get(pk = group_pk)
    color_serializer = GroupColorSerializer(group)
    
    contents = Content.objects.filter(Q(member__group__pk = group_pk)&(Q(title__contains = search)|Q(content__contains = search)|Q(member__name = search)))
    contents_serializer = ContentUserSerializer(contents, many = True)

    data = {}
    data['color'] = color_serializer.data['color']
    data['post'] = contents_serializer.data
    return Response(data)
    
