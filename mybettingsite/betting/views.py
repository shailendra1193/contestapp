# betting/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Match, Bet
from .forms import BetForm, Bet
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.shortcuts import render

def match_list(request):
    matches = Match.objects.all()
    return render(request, 'betting/match_list.html', {'matches': matches})


@login_required
def place_bet(request):
    if request.method == 'POST':
        form = BetForm(request.POST)
        if form.is_valid():
            bet = form.save(commit=False)
            bet.user = request.user
            match = bet.match  # The match is selected in the form
            match_datetime = timezone.make_aware(datetime.combine(match.match_date, match.start_time))

            # Check if current time is at least half an hour before match start time
            if match_datetime - timedelta(minutes=30) <= timezone.now():
                messages.error(request, 'Betting is closed for this match.')
                return render(request, 'betting/betting_closed.html', {'match': match})
            
            # Check if the user has already placed a bet on this match
            existing_bet = Bet.objects.filter(user=request.user, match=match).exists()
            if existing_bet:
                messages.error(request, 'You have already placed a bet on this match.')
                return redirect('betting:already_bet', match_id=match.id)

            bet.save()
            messages.success(request, 'Bet placed successfully!')
            return redirect('betting:home') 
    else:
        form = BetForm()

    return render(request, 'betting/place_bet.html', {'form': form})



# def place_bet(request):
#     match = get_object_or_404(Match)
#     user = request.user
#     now = timezone.now()
#     match_datetime = datetime.combine(match.match_date, match.start_time)
#     match_datetime = timezone.make_aware(match_datetime)  # Make it timezone aware if your project uses timezones

#     # Check if current time is at least half an hour before match start time
#     if match_datetime - timedelta(minutes=30) <= now:
#         # If not, redirect or show an error message
#         return render(request, 'betting/betting_closed.html', {'match': match})
    
#     # Check if the user has already placed a bet on this match
#     existing_bet = Bet.objects.filter(user=user, match=match).exists()
#     if existing_bet:
#         # Redirect to a page informing the user they've already bet
#         return redirect('betting:already_bet', match_id=match.id)

#     if request.method == 'POST':
#         form = BetForm(request.POST)
#         if form.is_valid():
#             bet = form.save(commit=False)
#             bet.user = request.user
#             bet.match = match
#             bet.save()
#             messages.success(request, 'Bet placed successfully!')
#             return redirect('betting:home')  # Redirect to a confirmation page or elsewhere

#     else:
#         form = BetForm(initial={'match': match})
#     return render(request, 'betting/place_bet.html', {'form': form, 'match': match})

@login_required
def view_bets(request):
    bets = Bet.objects.filter(user=request.user)
    return render(request, 'betting/view_bets.html', {'bets': bets})


def leaderboard(request):
    user_scores = User.objects.annotate(total_score=Sum('bet__points_awarded')).order_by('-total_score')
    return render(request, 'betting/leaderboard.html', {'user_scores': user_scores})


@login_required
def already_bet(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, 'betting/already_bet.html', {'match': match})

def home(request):
    print(request.user.is_authenticated) 
    # Your view logic here
    return render(request, 'betting/home.html')

def logout_confirmation(request):
    return render(request, 'betting/logout_confirmation.html')
    # redirect('betting:logout_confirmation')