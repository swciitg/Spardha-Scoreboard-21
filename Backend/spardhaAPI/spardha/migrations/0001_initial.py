# Generated by Django 4.0.3 on 2022-03-23 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(help_text='A - Football, Hockey, Cricket, Khokho, Basketball, Water Polo.  B - Lawn Tennis, Volleyball. C - Badminton, Table Tennis, Squash. D - Rest everything', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('overall_points', models.IntegerField(default=0)),
                ('type', models.IntegerField(choices=[(1, 'Boys'), (2, 'Girls')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, help_text='Enter 0 for upcoming and 1 for completed')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('winner', models.IntegerField(blank=True, choices=[(1, 'team1'), (2, 'team2')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('format', models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')])),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=11, null=True)),
                ('score_team1_game1', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team2_game1', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team1_game2', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team2_game2', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team1_game3', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team2_game3', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team1_game4', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team2_game4', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team1_game5', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team2_game5', models.CharField(blank=True, max_length=15, null=True)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game', to='spardha.matchc')),
            ],
        ),
        migrations.CreateModel(
            name='MatchD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, help_text='Enter 0 for upcoming and 1 for completed')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('hostels', models.ManyToManyField(to='spardha.hostel')),
                ('round', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.stage')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.sport')),
            ],
        ),
        migrations.AddField(
            model_name='matchc',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.sport'),
        ),
        migrations.AddField(
            model_name='matchc',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.stage'),
        ),
        migrations.AddField(
            model_name='matchc',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1', to='spardha.hostel'),
        ),
        migrations.AddField(
            model_name='matchc',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2', to='spardha.hostel'),
        ),
        migrations.CreateModel(
            name='MatchB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, help_text='Enter 0 for upcoming and 1 for completed')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('winner', models.IntegerField(blank=True, choices=[(1, 'team1'), (2, 'team2')], null=True)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.sport')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.stage')),
                ('team1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='spardha.hostel')),
                ('team2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='spardha.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='MatchA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, help_text='Enter 0 for upcoming and 1 for completed')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('score1', models.CharField(blank=True, max_length=15, null=True)),
                ('score2', models.CharField(blank=True, max_length=15, null=True)),
                ('winner', models.IntegerField(blank=True, choices=[(1, 'team1'), (2, 'team2')], null=True)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.sport')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.stage')),
                ('team1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='spardha.hostel')),
                ('team2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='spardha.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_team1', models.CharField(blank=True, max_length=15, null=True)),
                ('score_team2', models.CharField(blank=True, max_length=15, null=True)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.matchb')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('hostel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hostel', to='spardha.hostel')),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.matchd')),
            ],
            options={
                'unique_together': {('hostel', 'match')},
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('hostel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hostels', to='spardha.hostel')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spardha.sport')),
            ],
            options={
                'unique_together': {('hostel', 'sport')},
            },
        ),
    ]
