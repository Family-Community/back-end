# Generated by Django 4.2.4 on 2023-08-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_alter_createcontent_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createcontent',
            name='photo',
            field=models.ImageField(max_length=80, upload_to='user_photos/'),
        ),
    ]