from django.contrib import admin
from .models import Match, Bet

from django.contrib import admin
from .models import Match, Bet, Player, Team

class MatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'match_date', 'team_one', 'team_two', 'winning_team')
    fields = ['name', 'match_date', 'start_time', 'team_one', 'team_two', 'winning_team', 'best_batsman', 'best_bowler', 'best_allrounder']


admin.site.register(Match,MatchAdmin)
admin.site.register(Bet)
admin.site.register(Player)
admin.site.register(Team)