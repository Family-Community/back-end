from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('<int:pk>/contents/{int:memver_id}/create/',views.upload_content,name='creat_content'),
    # path('<int:pk>/contents/{int:memver_id}/{int:post_id}/update/', 업데이트뷰),
    # path('<int:pk>/contents/{int:memver_id}/{int:post_id}/delete/',삭제뷰),
    # path('<int:pk>/contents/{int:memver_id}/{int:post_id}/reaction/',리액션뷰)
]