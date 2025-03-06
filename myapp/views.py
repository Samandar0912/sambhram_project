from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, TemplateView, ListView
from myapp.models import *


# Create your views here.

# ================= INDEX =================
class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bgimg'] = EkranImages.objects.all()
        context['news'] = NewsArticle.objects.all()
        context['elon'] = ElonArticle.objects.all()
        context['havola'] = HavolaImages.objects.all()
        return context
    
# ================= NEWS =================

class AloqaView(TemplateView):
    template_name = "content/aloqa.html"

class HistoryView(TemplateView):
    template_name = "content/history.html"

class AboutView(TemplateView):
    template_name = "content/about.html"



# ================= NEWS =================
class NewsView(ListView):
    model = NewsArticle
    template_name = "news/news.html"
    context_object_name = "news_articles"
    ordering = ["-created"] 
    paginate_by = 2



class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = "news/news-detail.html"
    context_object_name = "news_article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = self.object.images.all()
        context["related_news"] = NewsArticle.objects.exclude(id=self.object.id).order_by('-created')[:5]
        return context




# ================= ELON =================

class ElonView(ListView):
    model = ElonArticle  # TO'G'RI MODEL
    template_name = "news/elon.html"  
    context_object_name = "elon_articles"
    ordering = ["-created"]  
    paginate_by = 2  





class ElonDetailView(DetailView):
    model = ElonArticle
    template_name = "news/elon-detail.html"
    context_object_name = "elon"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = self.object.images.all() if hasattr(self.object, 'images') else None
        context["related_elon"] = ElonArticle.objects.exclude(id=self.object.id).order_by('-created')[:5]
        return context




# ================= REKTORAT =================
class RektoratView(ListView):
    model = RectoratUserModel
    context_object_name = 'rektorat'
    template_name = "rektorat/rektorat/rektorat.html"


class RektoratDetailView(DetailView):
    model = RectoratUserModel
    context_object_name = 'rektoratUser'
    template_name = "rektorat/rektorat/rektorat-detail.html"




# ================= FAKULTET =================
class FakultetView(ListView):
    model = FacultetUserModel
    context_object_name = 'fakultet'
    template_name = "rektorat/fakultet/fakultet.html"


class FakultetDetailView(DetailView):
    model = FacultetUserModel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fakultet"] = FacultetUserModel.objects.all()
        context["userFakultet"] = FacultetInUserModel.objects.all()
        return context
    
    context_object_name = 'facultetUser'
    template_name = "rektorat/fakultet/detail.html"





# ================= MARKAZ =================
class MarkazView(ListView):
    model = MarkazUserModel
    context_object_name = 'markaz'
    template_name = "rektorat/markaz/markaz.html"

class MarkazDetailView(DetailView):
    model = MarkazUserModel
    context_object_name = 'markaz'
    template_name = "rektorat/markaz/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userMarkaz"] = MarkazInUserModel.objects.all()
        return context

# ================= BULIM =================
class BulimView(ListView):
    model = BulimUserModel
    context_object_name = 'bulim'
    template_name = "rektorat/bulim/bulim.html"

class BulimDetailView(DetailView):
    model = BulimUserModel
    context_object_name = 'bulim'
    template_name = "rektorat/bulim/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userBulim"] = BulimInUserModel.objects.all()
        return context

# ================= KAFEDRA =================
class KafedraView(ListView):
    model = KafedraUserModel
    context_object_name = 'kafedra'
    template_name = "rektorat/kafedra/kafedra.html"

class KafedraDetailView(DetailView):
    model = KafedraUserModel
    context_object_name = 'kafedra'
    template_name = "rektorat/kafedra/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userKafedra"] = KafedraInUserModel.objects.all()
        return context



# ================= FAOLIYAT =================
# ================= FAOLIYAT =================
# ================= FAOLIYAT =================

class FaoliyatView(TemplateView):
    template_name = "faoliyat/faoliyat.html"

class XalqaroFaoliyatView(TemplateView):
    template_name = "faoliyat/xf/xf.html"

class OquvFaoliyatView(TemplateView):
    template_name = "faoliyat/of/of.html"

class IlmiyFaoliyatView(TemplateView):
    template_name = "faoliyat/if/if.html"

class MoliyaviyFaoliyatView(TemplateView):
    template_name = "faoliyat/mf/mf.html"


# ================= TALIM =================
# ================= TALIM =================
# ================= TALIM =================


class TalimView(TemplateView):
    template_name = "talim/talim.html"
    
class KunduzView(TemplateView):
    template_name = "talim/kunduzgi/kunduzgi.html"
    
class SirqiView(TemplateView):
    template_name = "talim/sirtqi/sirtqi.html"
    
class BakalavrView(TemplateView):
    template_name = "talim/bakalavr/bakalavr.html"
    
class MagistrView(TemplateView):
    template_name = "talim/magistr/magistr.html"
    
class IkkinchiMutahasislikView(TemplateView):
    template_name = "talim/2_mustaxasis/2m.html"
    
class DoktaranturaView(TemplateView):
    template_name = "talim/doktarantura/doktarantura.html"
    

# ================= TALABALAR =================
# ================= TALABALAR =================
# ================= TALABALAR =================

class TalabalarView(TemplateView):
    template_name = "talabalar/talabalar.html"
    
    
class TalabalarSirqiView(TemplateView):
    template_name = "talabalar/sirtqi/sirtqi.html"
    
class TalabalarBakalavrView(TemplateView):
    template_name = "talabalar/bakalavr/bakalavr.html"
    
class TalabalarMagistrView(TemplateView):
    template_name = "talabalar/magistr/magistr.html"
    
class QaytaTiklashView(TemplateView):
    template_name = "talabalar/qayta_tiklash/qayta_tiklash.html"
    
