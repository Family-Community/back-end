from django.db import models
import uuid, hashlib
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile

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
    image_original = models.ImageField(upload_to="profile_original", null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.image_original:
            original_image = Image.open(self.image_original)
        
            max_size = (300, 300)
            
            width, height = original_image.size
            if width > height:
                diff = (width - height) // 2
                crop_box = (diff, 0, width - diff, height)
            else:
                diff = (height - width) // 2
                crop_box = (0, diff, width, height - diff)
            
            cropped_image = original_image.crop(crop_box)
            cropped_image.thumbnail(max_size, Image.LANCZOS)
            
            image_thumb_io = BytesIO()
            cropped_image.save(image_thumb_io, format='JPEG')  
            image_thumb = SimpleUploadedFile(
                name=f'{self.image_original.name.split(".")[0]}_thumb.jpg',  
                content=image_thumb_io.getvalue(),
                content_type='image/jpeg' 
            )
            self.image.save(image_thumb.name, image_thumb, save=False)
    
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if self.image_original:
    #         self.create_thumbnail()

    # def create_thumbnail(self):
    #     img = Image.open(self.image_original.path)

    #     max_size = (100, 100)
    #     img.thumbnail(max_size)

    #     thumb_io = BytesIO()
    #     img.save(thumb_io, format='JPEG')

    #     thumb_file = InMemoryUploadedFile(
    #         thumb_io, None, f'{self.image_original.name.split(".")[0]}_thumbnail.jpg',
    #         'image/jpeg', thumb_io.getbuffer().nbytes, None
    #     )

    #     self.image.save(thumb_file.name, thumb_file)