# Generated by Django 4.1.1 on 2022-11-07 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0039_alter_team_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_home_goal', models.IntegerField(default=0)),
                ('Team_visitor_goal', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date commented')),
                ('body', models.TextField()),
                ('Team_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='weblog_app.team')),
                ('Team_visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to='weblog_app.team')),
            ],
        ),
    ]