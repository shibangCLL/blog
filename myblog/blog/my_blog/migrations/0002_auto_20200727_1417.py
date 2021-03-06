# Generated by Django 2.2.14 on 2020-07-27 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img_link',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='img_url',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=0, upload_to='article/%Y%m', verbose_name='图片'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carousel',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='banner/%Y%m', verbose_name='轮播图'),
            preserve_default=False,
        ),
    ]
