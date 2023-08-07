from django.db import models
from family.models import Member
# Create your models here.


class Content(models.Model): 
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length= 20, blank= True, null=False)
    content = models.CharField(max_length=80 , blank =True, null=True)
    photo = models.TextField(default="")
    date= models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title
