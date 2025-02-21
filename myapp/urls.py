from django.urls import path
from myapp import views

app_name = "main"

urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    
    path('Yangiliklar/', views.NewsModelView.as_view(), name='news'),
    path("Yangiliklar/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),   
     
    path('Elonlar/', views.ElonModelView.as_view(), name='elon'),
    path("elon/<slug:slug>/", views.ElonDetailView.as_view(), name="elon_detail"),    
    
    path('Rektorat/', views.RektoratModelView.as_view(), name='rektorat'),
    path('Rektorat/<int:pk>/', views.RektoratDetailView.as_view(), name='rektorat_detail'),
     
    
    path('Fakultet/', views.FakultetModelView.as_view(), name='fakultet'),
    path('Fakultet/detail', views.FakultetDetailView.as_view(), name='fakultet-detail'),
    
    
    
]

