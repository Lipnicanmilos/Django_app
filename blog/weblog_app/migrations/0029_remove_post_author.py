# Generated by Django 4.1.1 on 2022-10-19 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0028_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]