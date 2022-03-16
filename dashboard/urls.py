"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from authO.views import logout
from homepage.views import HomepageListView
from persoonlijk.views import PersoonlijkView
from teams.views import TeamsView
from clusters.views import ClustersView
from organisatie.views import OrganisatieView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('authO.urls')),  
    path('', include('social_django.urls')),
    path('admin/', admin.site.urls),
    path('', HomepageListView.as_view(), name='home'),
    path('clusters/', ClustersView.as_view(), name='clusters'),
    path('organisatie/', OrganisatieView.as_view(), name='organisatie'),
    path('persoonlijk/', PersoonlijkView.as_view(), name='persoonlijk'),
    path('teams/', TeamsView.as_view(), name='teams'),
    path('', include('comments_feed.urls')),  
]