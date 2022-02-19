from django.shortcuts import render
from django.views.generic import ListView
from homepage.models import Organisatie

# Create your views here.

class TeamsView(ListView):
    template_name = 'teams/teams.html'
    model = Organisatie
