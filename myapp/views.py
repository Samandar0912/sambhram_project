from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, TemplateView, ListView
from myapp.models import *
from django.utils import translation
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def set_language(request):
    # POST yoki GET dan tilni olish
    user_language = request.POST.get('language') or request.GET.get('language', 'uz')
    logger.debug("Attempting to set language: %s", user_language)
    
    # Agar til mavjud bo'lmasa, standart 'uz' ni ishlatish
    if user_language not in dict(settings.LANGUAGES):
        user_language = 'uz'
    
    # Tilni faollashtirish
    translation.activate(user_language)
    
    # Cookie'ga tilni saqlash va redirect qilish
    response = redirect('/')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response


# ================= INDEX =================
class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bgimg'] = EkranImages.objects.all()
        context['news'] = NewsArticle.objects.all()
        context['elon'] = ElonArticle.objects.all()
        context['havola'] = HavolaImages.objects.all()
        context['galareyaIMG1'] = galareyaIMG1.objects.all()
        context['galareyaIMG2'] = galareyaIMG2.objects.all()
        context['galareyaIMG3'] = galareyaIMG3.objects.all()
        context['galareyaIMG4'] = galareyaIMG4.objects.all()
        return context
    
# ================= NEWS =================

class AloqaView(TemplateView):
    template_name = "content/aloqa.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['call'] = CallUserModel.objects.all()
        return context


class GalareyaView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context
    template_name = "content/galateya.html"


class HistoryView(TemplateView):
    template_name = "content/history.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = HistoryUniversity.objects.all()
        return context

    

class AboutView(TemplateView):
    template_name = "content/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUsUniversity.objects.all()
        return context

class StrukturaView(TemplateView):
    template_name = "content/struktura.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['struktura'] = Uiversitet_Struktura.objects.all()
        return context




class AboutMeView(TemplateView):
    template_name = "content/about-me.html"




# ================= NEWS =================
class NewsView(ListView):
    model = NewsArticle
    template_name = "news/news.html"
    context_object_name = "news_articles"
    ordering = ["-created"] 
    paginate_by = 16



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
    paginate_by = 16  





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
# ================= REKTORAT =================
# ================= REKTORAT =================

class RektoratMainView(TemplateView):
    template_name = "rektorat/rekttorat.html"


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
        context["userMarkaz"] = MarkazInUserModel.objects.filter(category=self.object)
        return context

# ================= BULIM =================
class BulimView(ListView):
    model = BulimUserModel
    context_object_name = 'bulim'
    template_name = "rektorat/bulim/bulim.html"

    def get_queryset(self):
        return BulimUserModel.objects.all() 
    
class BulimDetailView(DetailView):
    model = BulimUserModel
    context_object_name = 'bulim'
    template_name = "rektorat/bulim/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Joriy BulimUserModel ga tegishli ichki hodimlarni filter qilish
        context["userBulim"] = BulimInUserModel.objects.filter(category=self.object)
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
        context["userKafedra"] = KafedraInUserModel.objects.filter(category=self.object)
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
    
