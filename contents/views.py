from rest_framework.generics import CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContentSerializer,UpdateContentSerializer
from .models import CreateContent, UpdateContent

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


#게시글수정
class UpdateContentAPIView(UpdateAPIView):
    queryset = UpdateContent.objects.all()
    serializer_class = UpdateContentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
