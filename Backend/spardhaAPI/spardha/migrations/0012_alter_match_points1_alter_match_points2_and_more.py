# Generated by Django 4.0.3 on 2022-03-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spardha', '0011_alter_match_date_time_alter_match_all_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='points1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='points2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='score1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='score2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match_all',
            name='date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='match_all',
            name='points_awarded',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='sport',
            name='final_points',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='sport_league',
            name='final_points',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]