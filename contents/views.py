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
    

@api_view(['POST'])
def user_reaction(request, group_pk, member_pk, post_id, reaction_number):
    reaction = Reaction.objects.get(content__pk = post_id)
    
    if reaction_number == 1:
        if reaction.user_smile.filter(pk = member_pk).exists():
            reaction.user_smile.remove(Member.objects.get(pk = member_pk))
        else:
            reaction.user_smile.add(Member.objects.get(pk = member_pk))
    elif reaction_number == 2:
        if reaction.user_good.filter(pk = member_pk).exists():
            reaction.user_good.remove(Member.objects.get(pk = member_pk))
        else:
            reaction.user_good.add(Member.objects.get(pk = member_pk))
    elif reaction_number == 3:
        if reaction.user_sad.filter(pk = member_pk).exists():
            reaction.user_sad.remove(Member.objects.get(pk = member_pk))
        else:
            reaction.user_sad.add(Member.objects.get(pk = member_pk))
    elif reaction_number == 4:
        if reaction.user_heart.filter(pk = member_pk).exists():
            reaction.user_heart.remove(Member.objects.get(pk = member_pk))
        else:
            reaction.user_heart.add(Member.objects.get(pk = member_pk))
    elif reaction_number == 5:
        if reaction.user_worry.filter(pk = member_pk).exists():
            reaction.user_worry.remove(Member.objects.get(pk = member_pk))
        else:
            reaction.user_worry.add(Member.objects.get(pk = member_pk))
    elif reaction_number == 6:
        if reaction.user_check.filter(pk = member_pk).exists():
            reaction.user_check.remove(Member.objects.get(pk = member_pk))
        else:
            reaction.user_check.add(Member.objects.get(pk = member_pk))
    