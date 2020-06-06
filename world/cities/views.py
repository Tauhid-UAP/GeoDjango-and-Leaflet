from django.shortcuts import render
from django.views.generic import DetailView
from .models import City

# Create your views here.

class CitiesDetailView(DetailView):
    """
        City detail view.
    """
    template_name = 'cities/city_detail_view.html'
    model = City