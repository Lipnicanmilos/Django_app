# Generated by Django 4.1.1 on 2022-10-11 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0020_alter_manager_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='image',
            new_name='profile_image',
        ),
    ]
