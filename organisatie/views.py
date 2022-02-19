from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class OrganisatieView(TemplateView): 
    template_name = 'organisatie/organisatie.html'