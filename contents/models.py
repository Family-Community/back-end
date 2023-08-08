from django.db import models
from family.models import Member

#사진 저장 경로 설정
def user_photo_path(instance, filename):
    return f'user_photos/{instance.group._id}/{instance.member_id}/{filename}'

#게시글생성
class CreateContent(models.Model): 
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length= 20, blank= True, null=False)
    content = models.CharField(max_length=80 , blank =True, null=True)
    photo = models.ImageField(upload_to=user_photo_path,max_length=150,null=False)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

