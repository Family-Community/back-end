from django.urls import path
from . import views_member, views_group, views_member_generic


app_name = 'family'

urlpatterns = [

    # path('createfamily/', views_group.create_group),
    path('createfamily/', views_group.CreateGroup.as_view()), # 그룹 생성
    path('<int:pk>/delete/', views_group.DeleteGroup.as_view()), # 그룹 삭제
    path('<int:pk>/enter/<str:entry_number>/', views_group.entry_check), # 입장 번호 확인
    path('familycode/<str:family_code>/', views_group.return_id), # family_code -> pk 반환
    path('<int:group_pk>/<int:member_pk>/', views_member.get_member), # 멤버 정보 반환 + color
    path('<int:group_pk>/profile/', views_member.get_members), # 그룹 멤버 모두 반환 + color
    path('<int:group_pk>/profile/create/', views_member_generic.CreateMember.as_view()), # 그룹 내 프로필 생성
    path('profile/<int:pk>/update/', views_member_generic.UpdateMember.as_view()), # 프로필 수정
    path('profile/<int:pk>/delete/', views_member_generic.DeleteMember.as_view()), # 프로필 삭제
    path('allgroup/', views_group.all_group), # 모든 그룹 목록
    path('allmember/', views_member.all_member), # 모든 멤버 목록

]