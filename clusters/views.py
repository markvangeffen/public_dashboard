from django.shortcuts import render
from django.views.generic import ListView
from homepage.models import Organisatie

# Create your views here.

class ClustersView(ListView):
    template_name = 'clusters/clusters.html'
    model = Organisatie
