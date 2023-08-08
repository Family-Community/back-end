from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('<int:pk>/<int:member_id>/create/', views.CreateAPIView.create),
    path('<int:pk>/<int:member_id>/<int:post_id>/delete/',views.DestroyAPIView.destroy),
]


