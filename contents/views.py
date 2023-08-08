
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContentSerializer 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import CreateContent
import json


@api_view(['POST']) #게시글 생성
def create_content(request):
    try:
        data_object = json.load(request)
        title = data_object['title']
        content = data_object['content']
        photo = data_object['photo']
        contents = CreateContent(title=title, content=content,photo=photo)
        contents.save()
        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE']) #게시글 삭제
def delete_content(request, pk):
    content = CreateContent.objects.get(pk=pk)
    content.delete()
    return Response(status=status.HTTP_200_OK)


from rest_framework.generics import CreateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContentSerializer
from .models import CreateContent

#게시글생성
class CreateContentAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    queryset = CreateContent.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED)

#게시글삭제
class DeleteContentAPIView(DestroyAPIView):
    queryset = CreateContent.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


