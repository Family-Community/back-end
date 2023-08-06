from django.urls import path
from . import views_member
from . import views_group

app_name = 'family'

urlpatterns = [
    path('createfamily/', views_group.create_group),
    path('<str:family_name>/delete/', views_group.delete_group),
    path('<str:family_name>/<str:entry_number>/', views_group.entry_check),
    path('<str:family_name>/profile/create/', views_member.create_member),
    path('<str:family_name>/profile/<int:member_id>/update/', views_member.update_member),
    path('<str:family_name>/profile/<int:member_id>/delete/', views_member.delete_member),
]