from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _




# Ekran Rasmi
class EkranImages(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Media/ekran_IMG/')

    class Meta:
        verbose_name = "Ekran Rasmi"
        verbose_name_plural = "Ekran Rasmlari"

    def __str__(self):
        return self.name







# News model

class NewsArticle(models.Model):
    title = models.CharField(max_length=250, verbose_name="Sarlovha")
    body = models.TextField(verbose_name="text")
    photo = models.ImageField(upload_to="Media/news", verbose_name="Rasm")
    created = models.DateTimeField(auto_now=True,)
    past_times = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="eski yangilik bolsa sanasi") 
    views = models.PositiveIntegerField(default=0)    

    class Meta:
        ordering = ["-id"]
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("NewsArticle_detail", kwargs={"pk": self.pk})



class NewsImage(models.Model):
    news = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="Media/news")







# Elon model

class ElonArticle(models.Model):
    name = models.CharField(max_length=100, verbose_name="vaziyat")
    title = models.CharField(max_length=250, verbose_name="Sarlovha")
    body = models.TextField(verbose_name="text")
    photo = models.ImageField(upload_to="Media/news", verbose_name="Rasm")
    created = models.DateTimeField(auto_now=True,)
    past_times = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="eski yangilik bolsa sanasi") 
    views = models.PositiveIntegerField(default=0)    

    class Meta:
        ordering = ["-id"]
        verbose_name = "Elon"
        verbose_name_plural = "Elonlar"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ElonArticle_detail", kwargs={"pk": self.pk})



class ElonImage(models.Model):
    news = models.ForeignKey(ElonArticle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="Media/news")




# Foydali havola model
class HavolaImages(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Media/FH/')
    link = models.CharField(max_length=250, verbose_name="havola linki")

    class Meta:
        verbose_name = "Foydali havola"
        verbose_name_plural = "Foydali havola"

    def __str__(self):
        return self.name



