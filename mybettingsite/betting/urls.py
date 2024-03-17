# betting/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import logout_confirmation  

urlpatterns = [
    path('match_list/', views.match_list, name='match_list'),
    path('', views.home, name='home'),
    path('mybets/', views.view_bets, name='view_bets'),
    path('place_bet/', views.place_bet, name='place_bet'),
    path('already_bet/<int:match_id>/', views.already_bet, name='already_bet'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('logout/', LogoutView.as_view(next_page='logout_confirmation'), name='logout'),
    
    
    
]
