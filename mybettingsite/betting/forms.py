# betting/forms.py

from django import forms
from .models import Bet, Match, Player

class BetForm(forms.ModelForm):
    match = forms.ModelChoiceField(queryset=Match.objects.all(), empty_label="Select a Match")
    class Meta:
        model = Bet
        fields = ['match', 'chosen_winner', 'best_batsman', 'best_bowler', 'best_allrounder']
        widgets = {
            'match': forms.HiddenInput(),  # Assuming the match is pre-selected
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['best_batsman'].queryset = Player.objects.filter(role='batsman')
        self.fields['best_bowler'].queryset = Player.objects.filter(role='bowler')
        self.fields['best_allrounder'].queryset = Player.objects.filter(role='allrounder')
