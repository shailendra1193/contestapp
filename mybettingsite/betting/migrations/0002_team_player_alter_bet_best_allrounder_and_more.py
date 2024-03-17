# Generated by Django 4.0.1 on 2024-03-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='betting.team')),
            ],
        ),
        migrations.AlterField(
            model_name='bet',
            name='best_allrounder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bets_best_allrounder', to='betting.player'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='best_batsman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bets_best_batsman', to='betting.player'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='best_bowler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bets_best_bowler', to='betting.player'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='chosen_winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='betting.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='betting.team'),
        ),
    ]