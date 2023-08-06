from django.urls import path
from . import views_member
from . import views_group

app_name = 'family'

urlpatterns = [
    path('createfamily/', views_group.create_group),
    path('{:family_code}/profile/create/')
]