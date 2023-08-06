from django.db import models

# Create your models here.
class Group(models.Model):
    family_name = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    entry_number = models.CharField(max_length=10)

class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    img = models.ImageField(null=True, upload_to="", blank=True)