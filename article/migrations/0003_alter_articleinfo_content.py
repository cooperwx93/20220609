# Generated by Django 4.0.5 on 2022-06-09 10:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articleinfo_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleinfo',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容'),
        ),
    ]