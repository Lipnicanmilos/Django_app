# Generated by Django 4.1.1 on 2022-10-17 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weblog_app', '0022_alter_manager_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
