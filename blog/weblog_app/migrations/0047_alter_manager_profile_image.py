# Generated by Django 4.1.1 on 2022-11-15 09:24

from django.db import migrations, models
import weblog_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0046_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='profile_image',
            field=models.ImageField(default='managers/default.jpg', upload_to='managers/'),
        ),
    ]
