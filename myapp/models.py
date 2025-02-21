from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField




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
    past_times = models.DateTimeField(auto_now_add=False, blank=True, verbose_name="eski yangilik bolsa sanasi") 
    views = models.PositiveIntegerField(default=0)    
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("NewsArticle_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Agar slug bo‘sh bo‘lsa, avtomatik yaratiladi
            self.slug = slugify(self.title)

        original_slug = self.slug
        counter = 1
        while NewsArticle.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1

        super().save(*args, **kwargs)



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
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Elon"
        verbose_name_plural = "Elonlar"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ElonArticle_detail", kwargs={"slug": self.slug})
    
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Agar slug bo‘sh bo‘lsa, avtomatik yaratiladi
            self.slug = slugify(self.title)

        original_slug = self.slug
        counter = 1
        while ElonArticle.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1

        super().save(*args, **kwargs)
    



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



class RektoratCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nomi")
    
    class Meta:
        verbose_name = "Universitet Kategorya"
        verbose_name_plural = "Universitet Kategorya"

    def __str__(self):
        return self.name


class RectoratUserModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="F.I.SH")
    body = models.TextField(verbose_name="Malumot")
    rang = models.CharField(max_length=150, verbose_name="lavozim")
    number = PhoneNumberField(unique=True, blank=False, null=False, verbose_name="Tell number")
    photo = models.ImageField(upload_to='Media/Rektorat/')
    email = models.EmailField(max_length=254, verbose_name="email")
    category = models.ForeignKey(RektoratCategory, on_delete=models.CASCADE)
 
    def get_absolute_url(self):
        return reverse('main:rektorat_detail', args=[str(self.pk)])
 
    class Meta:
        verbose_name = "Rektorat Hodimlar"
        verbose_name_plural = "Rektorat Hodimlar"

    def __str__(self):
        return self.name



class UserModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="F.I.SH")
    rang = models.CharField(max_length=150, verbose_name="lavozim")
    photo = models.ImageField(upload_to='Media/Rektorat/')
    number = PhoneNumberField(unique=True, blank=False, null=False, verbose_name="Tell number")
    email = models.EmailField(max_length=254, verbose_name="email")
    tg = models.CharField(max_length=150, verbose_name="tg manzil")
    category = models.ForeignKey(RectoratUserModel, on_delete=models.CASCADE)
 
 
    def get_absolute_url(self):
        return reverse('main:UserModel_detail', args=[str(self.pk)])
    
    class Meta:
        verbose_name = "Rektorat ichki Hodimlar"
        verbose_name_plural = "Rektorat ichki Hodimlar"

    def __str__(self):
        return self.name