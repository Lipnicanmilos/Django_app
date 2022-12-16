# Generated by Django 4.1.1 on 2022-11-15 12:37

from django.db import migrations, models
import weblog_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0051_alter_manager_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='profile_image',
            field=models.ImageField(default='managers/default.png', upload_to='managers/', validators=[weblog_app.models.validate_image]),
        ),
    ]