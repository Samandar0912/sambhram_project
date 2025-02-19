from django.shortcuts import render
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
