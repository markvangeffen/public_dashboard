from django.views.generic import TemplateView
from django.views.generic import ListView

from homepage.models import Organisatie

# transformed to ListView with model = Organisatie
class HomepageListView(ListView):
    template_name = 'dashboard/base.html'
    template_name = 'homepage/index.html'
    model = Organisatie
