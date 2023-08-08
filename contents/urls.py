from django.urls import path
from . import views
from .views import *

app_name = 'contents'

urlpatterns = [
    path('<int:pk>/<int:member_id>/create/', CreateContentAPIView.as_view()),
    path('<int:pk>/<int:member_id>/<int:post_id>/delete/',DeleteContentAPIView.as_view()),
]


