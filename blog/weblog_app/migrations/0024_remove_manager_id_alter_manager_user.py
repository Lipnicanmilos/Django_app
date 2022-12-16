# Generated by Django 4.1.1 on 2022-10-17 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weblog_app', '0023_alter_manager_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='id',
        ),
        migrations.AlterField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
