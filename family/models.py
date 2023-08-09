from django.db import models
import uuid, hashlib

def generate_hash():
    id = str(uuid.uuid4())
    hash = hashlib.sha256(id.encode())
    return hash.hexdigest()

# Create your models here.
class Group(models.Model):
    family_name = models.CharField(max_length=10)
    family_code = models.CharField(max_length=64, default=generate_hash, editable=False)
    color = models.CharField(max_length=7)
    entry_number = models.CharField(max_length=4)

    def save(self, *args, **kwargs):
        if not self.family_code:
            self.family_code = generate_hash()
        super().save(*args, **kwargs)

class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
