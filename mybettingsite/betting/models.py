# betting/models.py

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#players 1
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)  # E.g., "Batsman", "Bowler", "Allrounder"

    def __str__(self):
        return f"{self.name} ({self.role})"

class Match(models.Model):
    name = models.CharField(max_length=100)
    match_date = models.DateField()
    start_time = models.TimeField()
    team_one = models.ForeignKey('Team', related_name='home_matches', on_delete=models.CASCADE)
    team_two = models.ForeignKey('Team', related_name='away_matches', on_delete=models.CASCADE)
    winning_team = models.ForeignKey('Team', related_name='won_matches', on_delete=models.SET_NULL, null=True, blank=True)
    best_batsman = models.ForeignKey('Player', related_name='matches_best_batsman', on_delete=models.SET_NULL, null=True, blank=True)
    best_bowler = models.ForeignKey('Player', related_name='matches_best_bowler', on_delete=models.SET_NULL, null=True, blank=True)
    best_allrounder = models.ForeignKey('Player', related_name='matches_best_allrounder', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} on {self.match_date}"

class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    chosen_winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    best_batsman = models.ForeignKey(Player, related_name='best_batsman', on_delete=models.SET_NULL, null=True, blank=True)
    best_bowler = models.ForeignKey(Player, related_name='best_bowler', on_delete=models.SET_NULL, null=True, blank=True)
    best_allrounder = models.ForeignKey(Player, related_name='best_allrounder', on_delete=models.SET_NULL, null=True, blank=True)
    points_awarded = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'match')

    def __str__(self):
        return f"Bet by {self.user.username} on {self.match}"
    
# @receiver(post_save, sender=Match)
# def update_scores(sender, instance, **kwargs):
#     # Place your score calculation logic here.
#     # This function will be called every time a Match instance is saved.
