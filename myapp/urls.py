from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from myapp import views

app_name = "main"

urlpatterns = (
    path('', views.IndexView.as_view(), name="index"),
    path('set_language/', views.set_language, name='set_language'),
    path('Aloqa/', views.AloqaView.as_view(), name="aloqa"),
    path('Galareya/', views.GalareyaView.as_view(), name="galareya"),
    
    path('Struktura/', views.StrukturaView.as_view(), name="struktura"),
    path('Universitet-Tarixi/', views.HistoryView.as_view(), name="history"),
    path('Universitet-Haqida/', views.AboutView.as_view(), name="about"),
    path('Biz-Haqimizda/', views.AboutMeView.as_view(), name="about-me"),
    
    path('Yangiliklar/', views.NewsView.as_view(), name='news'),
    path("Yangiliklar/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),   
     
    path('Elonlar/', views.ElonView.as_view(), name='elon'),
    path("elon/<slug:slug>/", views.ElonDetailView.as_view(), name="elon_detail"),    
    
    path('Rektorat-main/', views.RektoratMainView.as_view(), name='rektorat_main'),
    path('Rektorat/', views.RektoratView.as_view(), name='rektorat'),
    path('Rektorat/<int:pk>/', views.RektoratDetailView.as_view(), name='rektorat_detail'),
     
    path('Fakultet/', views.FakultetView.as_view(), name='fakultet'),
    path('Fakultet/<int:pk>/', views.FakultetDetailView.as_view(), name='fakultet_detail'),
    
    path('Markaz/', views.MarkazView.as_view(), name='markaz'),
    path('Markaz/<int:pk>/', views.MarkazDetailView.as_view(), name='markaz_detail'),
    
    path('Bo\'limlar/', views.BulimView.as_view(), name='bulim'),
    path('Bo\'limlar/<int:pk>/', views.BulimDetailView.as_view(), name='bulim_detail'),
    
    path('Kafedralar/', views.KafedraView.as_view(), name='kafedra'),
    path('Kafedralar/<int:pk>/', views.KafedraDetailView.as_view(), name='kafedra_detail'),
    
    path('Faoliyat/', views.FaoliyatView.as_view(), name='faoliyat'),
    path('Faoliyat/Xalqaro-faoliyat/', views.XalqaroFaoliyatView.as_view(), name='xf'),
    path('Faoliyat/Oquv-faoliyat/', views.OquvFaoliyatView.as_view(), name='of'),
    path('Faoliyat/Moliyaviy-faoliyat/', views.MoliyaviyFaoliyatView.as_view(), name='mf'),
    path('Faoliyat/Ilmiy-faoliyat/', views.IlmiyFaoliyatView.as_view(), name='if'),
    
    path('Talim/', views.TalimView.as_view(), name='talim'),
    path('Talim/Kunduzki-talim/', views.KunduzView.as_view(), name='kunduzki'),
    path('Talim/Sritqi-talim/', views.SirqiView.as_view(), name='sirtqi'),
    path('Talim/Bakalavr/', views.BakalavrView.as_view(), name='bakalavr'),
    path('Talim/Magistratura/', views.MagistrView.as_view(), name='magistr'),
    path('Talim/2-Mutaxasislik/', views.IkkinchiMutahasislikView.as_view(), name='2m'),
    path('Talim/Doktarantura/', views.DoktaranturaView.as_view(), name='doc'),
    
    path('Talabalar/', views.TalabalarView.as_view(), name='talabalar'),
    path('Talabalar/Sirtqi-talim/', views.TalabalarSirqiView.as_view(), name='T_Sirqi'),
    path('Talabalar/Bakalavir/', views.TalabalarBakalavrView.as_view(), name='T_Bakalavr'),
    path('Talabalar/Magistratura/', views.TalabalarMagistrView.as_view(), name='T_Magistr'),
    path('Talabalar/O\'qishni-ko\'chirish-vaqayta-tiklash/', views.QaytaTiklashView.as_view(), name='T_qayta-tiklash'),
)
