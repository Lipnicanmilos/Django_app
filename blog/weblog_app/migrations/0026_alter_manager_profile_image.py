# Generated by Django 4.1.1 on 2022-10-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0025_manager_id_alter_manager_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='profile_image',
            field=models.ImageField(blank=True, default='managers/default.jpg', upload_to='managers/'),
        ),
    ]
