# Generated by Django 4.1.1 on 2022-10-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0007_rename_manager_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
    ]