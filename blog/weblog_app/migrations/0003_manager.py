# Generated by Django 4.1.1 on 2022-10-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0002_alter_comment_date_alter_post_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstusername_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date registred')),
            ],
        ),
    ]