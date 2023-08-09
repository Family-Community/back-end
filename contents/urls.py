from django.urls import path
from . import views
from .views import *

app_name = 'contents'

urlpatterns = [
    path('', AllContent.as_view()), # 모든 게시글 확인,
    path('<int:group_pk>/<int:member_pk>/create/', CreateContent.as_view()), # 게시글 작성
    path('<int:group_pk>/<int:member_pk>/<int:post_id>',RetrieveUpdateDestroyAPIView.as_view()), # 게시글 수정/삭제
    path('<int:group_pk>/', views.get_contents), # 그룹 내 게시글 확인
    path('<int:group_pk>/<str:search>/', views.search_contents), # 게시물 검색
]


