# Generated by Django 4.0.3 on 2022-03-15 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spardha', '0002_remove_score_hostels_score_hostel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='hostels',
            new_name='hostel',
        ),
    ]
