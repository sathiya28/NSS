# Generated by Django 3.2.7 on 2021-12-28 15:43

from django.db import migrations, models
import nss.models


class Migration(migrations.Migration):

    dependencies = [
        ('nss', '0003_alter_imageupload_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='images',
            field=models.ImageField(null=True, upload_to=nss.models.image_file_path),
        ),
    ]
