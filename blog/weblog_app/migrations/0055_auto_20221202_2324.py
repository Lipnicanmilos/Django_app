# Generated by Django 3.2.16 on 2022-12-02 22:24

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_app', '0054_auto_20221202_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='new_season_name',
            new_name='season_name',
        ),
        migrations.AlterField(
            model_name='match',
            name='Team_home',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='season_name', chained_model_field='season_names', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='weblog_app.team'),
        ),
    ]
