# Generated by Django 4.0.5 on 2022-06-12 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_alter_like_liked_or_not'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]