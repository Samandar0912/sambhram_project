from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, TemplateView, ListView
from myapp.models import *


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # `super()` bilan asosiy `context` ni olamiz
        context['bgimg'] = EkranImages.objects.all()
        context['news'] = NewsArticle.objects.all()
        context['elon'] = ElonArticle.objects.all()
        context['havola'] = HavolaImages.objects.all()
        return context
    




class NewsModelView(ListView):
    model = NewsArticle
    template_name = "news/news.html"
    context_object_name = "news_articles"
    ordering = ["-created"] 
    paginate_by = 12 



class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = "news/news-detail.html"
    context_object_name = "news_article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = self.object.images.all()
        context["related_news"] = NewsArticle.objects.exclude(id=self.object.id).order_by('-created')[:5]
        return context





class ElonModelView(ListView):
    model = ElonArticle  # TO'G'RI MODEL
    template_name = "news/elon.html"  
    context_object_name = "elon_articles"
    ordering = ["-created"]  
    paginate_by = 12  





class ElonDetailView(DetailView):
    model = ElonArticle
    template_name = "news/elon-detail.html"
    context_object_name = "elon"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = self.object.images.all() if hasattr(self.object, 'images') else None
        context["related_elon"] = ElonArticle.objects.exclude(id=self.object.id).order_by('-created')[:5]
        return context




class RektoratModelView(ListView):
    model = RectoratUserModel
    context_object_name = 'rektorat'
    template_name = "rektorat/rektorat.html"


class RektoratDetailView(DetailView):
    model = RectoratUserModel
    context_object_name = 'rektoratUser'
    template_name = "rektorat/rektorat-detail.html"




class FakultetModelView(TemplateView):
    template_name = "rektorat/fakultet/fakultet.html"


class FakultetDetailView(TemplateView):
    template_name = "rektorat/fakultet/fakultet-detail.html"



