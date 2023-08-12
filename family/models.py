from django.db import models
import uuid, hashlib
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

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
    image_thumbnail = models.ImageField(upload_to="profile_thumbnail", null=True, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            # 이미지를 업로드한 경우에만 이미지를 축소하여 thumbnail을 생성합니다.
            self.create_thumbnail()

    def create_thumbnail(self):
        if not self.image_thumbnail:
            img = Image.open(self.image.path)

            # 이미지 크기 조정
            max_size = (100, 100)
            img.thumbnail(max_size)

            # BytesIO를 사용하여 메모리에 임시 파일 생성
            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG')

            # 이미지를 파일 필드에 저장
            thumb_file = InMemoryUploadedFile(
                thumb_io, None, f'{self.image.name.split(".")[0]}_thumbnail.jpg',
                'image/jpeg', thumb_io.getbuffer().nbytes, None
            )

            self.image_thumbnail.save(thumb_file.name, thumb_file, save=False)
            self.save()