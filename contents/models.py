from django.db import models

# Create your models here.

class CreateContent(models.Model): #피드 작성하기
    title = models.CharField(max_length= 20, blank= True, null=False)
    content = models.CharField(max_length=80 , blank =True, null=True)
    photo = models.TextField(default="")
    date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title   