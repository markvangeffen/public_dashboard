from django.urls import path
from . import views

# To disable Django's login screen:
from django.contrib.auth.decorators import login_required
from django.contrib import admin

# admin.autodiscover()
# admin.site.login = login_required(admin.site.login)

urlpatterns = [ 
    path('logout/', views.logout, name='logout'),
]

