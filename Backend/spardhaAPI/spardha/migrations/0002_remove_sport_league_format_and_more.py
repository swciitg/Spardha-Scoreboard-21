# Generated by Django 4.0.3 on 2022-03-16 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spardha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport_league',
            name='format',
        ),
        migrations.RemoveField(
            model_name='sport_league',
            name='hostels',
        ),
        migrations.DeleteModel(
            name='Points',
        ),
        migrations.DeleteModel(
            name='Sport_League',
        ),
    ]
