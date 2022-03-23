# Generated by Django 4.0.3 on 2022-03-22 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spardha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_all',
            name='scores',
        ),
        migrations.CreateModel(
            name='Match_set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, help_text='Enter 0 for upcoming and 1 for completed')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('set', models.IntegerField(choices=[(1, 'Set1'), (2, 'Set2'), (3, 'Set3'), (4, 'Set4'), (5, 'Set5')])),
                ('score1', models.IntegerField(blank=True, null=True)),
                ('score2', models.IntegerField(blank=True, null=True)),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.format')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game', to='spardha.sport')),
                ('team1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='spardha.hostel')),
                ('team2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='spardha.hostel')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='spardha.hostel')),
            ],
        ),
    ]
