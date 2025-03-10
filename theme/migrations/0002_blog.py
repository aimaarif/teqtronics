# Generated by Django 5.1.6 on 2025-02-28 05:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('image', models.ImageField(upload_to='blogs/')),
                ('published_date', models.DateField(auto_now_add=True)),
                ('comment_count', models.IntegerField(default=0)),
            ],
        ),
    ]
