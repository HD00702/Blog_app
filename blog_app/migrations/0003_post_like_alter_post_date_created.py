# Generated by Django 4.0.5 on 2022-06-10 06:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0002_alter_post_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]