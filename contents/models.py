from django.db import models
from family.models import Member,Group

#사진 저장 경로 설정
def user_photo_path(instance, filename):
    return f'user_photos/{instance.member.pk}/{filename}'


class Content(models.Model): 
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length= 20, blank= True, null=False)
    content = models.CharField(max_length=80 , blank =True, null=True)
    photo = models.ImageField(upload_to=user_photo_path,max_length=150,null=False)
    date= models.DateTimeField(auto_now_add=True)
    user_smile = models.ManyToManyField(Member, related_name='smile_content',)
    user_good = models.ManyToManyField(Member, related_name='good_content')
    user_sad = models.ManyToManyField(Member, related_name='sad_content')
    user_heart = models.ManyToManyField(Member, related_name='heart_content')
    user_worry = models.ManyToManyField(Member, related_name='worry_content')
    user_check = models.ManyToManyField(Member, related_name='check_content')
    smile_cnt = models.IntegerField(default= 0)
    good_cnt = models.IntegerField(default= 0)
    sad_cnt = models.IntegerField(default= 0)
    heart_cnt = models.IntegerField(default= 0)
    worry_cnt = models.IntegerField(default= 0)
    check_cnt = models.IntegerField(default= 0)

    def __str__(self):
        return self.title
    

# class Reaction(models.Model):
#     content = models.OneToOneField(Content, on_delete=models.CASCADE)
#     user_smile = models.ManyToManyField(Member, related_name='smile_content',)
#     user_good = models.ManyToManyField(Member, related_name='good_content')
#     user_sad = models.ManyToManyField(Member, related_name='sad_content')
#     user_heart = models.ManyToManyField(Member, related_name='heart_content')
#     user_worry = models.ManyToManyField(Member, related_name='worry_content')
#     user_check = models.ManyToManyField(Member, related_name='check_content')