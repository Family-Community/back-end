from django.urls import path
from . import views_member, views_group, views_member_generic

app_name = 'family'

urlpatterns = [
    # path('createfamily/', views_group.create_group),
    path('createfamily/', views_group.CreateGroup.as_view()),
    path('<int:pk>/delete/', views_group.DeleteGroup.as_view()),
    path('<int:pk>/enter/<str:entry_number>/', views_group.entry_check),
    path('<int:pk>/profile/', views_member.get_members),
    path('<int:group_pk>/profile/create/', views_member_generic.CreateMember.as_view()),
    # path('<int:group_pk>/profile/<int:member_pk>/update/', views_member.update_member),
    # path('<int:group_pk>/profile/<int:member_pk>/delete/', views_member.delete_member),
    path('<int:group_pk>/profile/<int:pk>/', views_member_generic.MemberDetail.as_view()),
    path('<int:group_pk>/<int:member_pk>/', views_member.get_member),
    path('allgroup/', views_group.all_group),
    path('allmember/', views_member.all_member),
]