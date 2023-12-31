from django.urls import path
from . import views
from .views import *

app_name = 'contents'

urlpatterns = [
    path('', AllContent.as_view()), # 모든 게시글 확인,
    path('<int:group_pk>/<int:member_pk>/create/', CreateContent.as_view()), # 게시글 작성
    path('<int:group_pk>/<int:member_pk>/<int:post_pk>/update/', UpdateContent.as_view()), # 게시글 수정
    path('<int:group_pk>/<int:member_pk>/<int:post_pk>/delete/', DeleteContent.as_view()), # 게시글 삭제
    path('<int:group_pk>/', views.get_contents), # 그룹 내 게시글 확인
    path('<int:group_pk>/<str:search>/', views.search_contents), # 게시물 검색
    path('<int:group_pk>/<int:member_pk>/<int:post_pk>/reaction/<int:reaction_num>/', views.react), # 게시글 반응 작성
    path('getpost/<int:post_id>/', views.get_post), # 게시글 반환
    path('getuserpost/<int:member_pk>/', views.get_user_post), # 한 유저의 게시글 반환
]