from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Thing
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class ThingsListView(ListView):
    template_name = 'things_list.html'
    model = Thing
    context_object_name = "data"

class ThingDetailsView(DetailView):
    template_name = 'thing_details.html'
    model = Thing

