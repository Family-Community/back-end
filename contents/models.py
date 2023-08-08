from django.db import models
from ..family.models import *

# Create your models here.

# 피드 작성하기
class Content(models.Model): 
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length= 20, blank= True, null=False)
    content = models.CharField(max_length=80 , blank =True, null=True)
    photo = models.TextField(default="")
    date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

# 리액션
class Reaction(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
