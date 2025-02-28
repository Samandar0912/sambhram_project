from django.urls import path
from myapp import views

app_name = "main"

urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    
    path('Yangiliklar/', views.NewsView.as_view(), name='news'),
    path("Yangiliklar/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),   
     
    path('Elonlar/', views.ElonView.as_view(), name='elon'),
    path("elon/<slug:slug>/", views.ElonDetailView.as_view(), name="elon_detail"),    
    
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
    path('Faoliyat/Xalqaro-faoliyat', views.XalqaroFaoliyatView.as_view(), name='xf'),
    path('Faoliyat/Oquv-faoliyat', views.OquvFaoliyatView.as_view(), name='of'),
    
    
]

