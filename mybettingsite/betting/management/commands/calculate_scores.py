from django.core.management.base import BaseCommand, CommandError
from betting.models import Match, Bet
from django.db.models import F

class Command(BaseCommand):
    help = 'Calculates scores for bets on a given match'

    def add_arguments(self, parser):
        parser.add_argument('match_id', type=int)

    def handle(self, *args, **options):
        match_id = options['match_id']
        match = Match.objects.get(id=match_id)

        for bet in Bet.objects.filter(match=match):
            score = 0
            if bet.chosen_winner == match.winning_team:
                score += 1000
            if bet.best_batsman == match.best_batsman:
                score += 500
            if bet.best_bowler == match.best_bowler:
                score += 500
            if bet.best_allrounder == match.best_allrounder:
                score += 500
            
            bet.points_awarded = F('points_awarded') + score
            bet.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully calculated scores for match {match_id}'))
