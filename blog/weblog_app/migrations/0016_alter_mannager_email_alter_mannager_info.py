# Generated by Django 4.1.1 on 2022-10-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0015_mannager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mannager',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mannager',
            name='info',
            field=models.TextField(null=True),
        ),
    ]