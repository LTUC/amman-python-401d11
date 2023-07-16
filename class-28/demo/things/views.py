from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Thing
from django.urls import reverse_lazy, reverse
# Create your views here.

class ThingListView(ListView):
    template_name = 'things_list.html'
    model = Thing


class ThingDetailView(DetailView):
    template_name = 'things_detail.html'
    model = Thing

class ThingCreateView(CreateView):
    template_name = 'things_create.html'
    model = Thing
    fields=['name','rank','reviewer']

class ThingUpdateView(UpdateView):    
    template_name = 'things_update.html'
    model = Thing
    fields='__all__'
    success_url = reverse_lazy('thing_list')
    # success_url = reverse('thing_list')


class ThingDeleteView(DeleteView):
    template_name = 'things_delete.html'
    model = Thing
    success_url = reverse_lazy('thing_list') #mandatory



