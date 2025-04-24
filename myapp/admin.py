from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    EkranImages, NewsArticle, NewsImage, ElonArticle, ElonImage, HavolaImages,
    RektoratCategory, RectoratUserModel, UserModel, FacultetUserModel,
    FacultetInUserModel, MarkazUserModel, MarkazInUserModel, BulimUserModel,
    BulimInUserModel, KafedraUserModel, KafedraInUserModel, HistoryUniversity, AboutUsUniversity, CallUserModel, Video
)

@admin.register(Video)
class EkranImagesAdmin(admin.ModelAdmin):
    list_display = ('title',)

    
# Ekran Rasmi (tarjima qilinmaydi)
@admin.register(EkranImages)
class EkranImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')
    search_fields = ('name',)
    list_per_page = 20

# Yangiliklar
@admin.register(NewsArticle)
class NewsArticleAdmin(TranslationAdmin):
    list_display = ('title', 'created', 'views', 'slug')
    list_display_links = ('title', 'created')
    list_filter = ('created',)
    search_fields = ('title_uz', 'title_en', 'title_ru', 'body_uz', 'body_en', 'body_ru')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
    readonly_fields = ('created', 'views')
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('title_uz', 'title_en', 'title_ru', 'body_uz', 'body_en', 'body_ru', 'photo', 'slug')
        }),
        ('Vaqt va statistika', {
            'fields': ('created', 'past_times', 'views')
        }),
    )

@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('news', 'image')
    search_fields = ('news__title_uz', 'news__title_en', 'news__title_ru')
    list_per_page = 20

# E'lonlar
@admin.register(ElonArticle)
class ElonArticleAdmin(TranslationAdmin):
    list_display = ('name', 'title', 'created', 'views', 'slug')
    list_filter = ('created',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'title_uz', 'title_en', 'title_ru', 'body_uz', 'body_en', 'body_ru')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
    readonly_fields = ('created', 'views')
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'title_uz', 'title_en', 'title_ru', 'body_uz', 'body_en', 'body_ru', 'photo', 'slug')
        }),
        ('Vaqt va statistika', {
            'fields': ('created', 'past_times', 'views')
        }),
    )

@admin.register(ElonImage)
class ElonImageAdmin(admin.ModelAdmin):
    list_display = ('news', 'image')
    search_fields = ('news__title_uz', 'news__title_en', 'news__title_ru')
    list_per_page = 20

# Foydali havolalar
@admin.register(HavolaImages)
class HavolaImagesAdmin(TranslationAdmin):
    list_display = ('name_uz', 'link', 'img')
    search_fields = ('name_uz', 'name_en', 'name_ru', 'link')
    list_per_page = 20
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'link', 'img')
        }),
    )



# Rektorat Kategoriyasi
@admin.register(RektoratCategory)
class RektoratCategoryAdmin(admin.ModelAdmin):  # TranslationAdmin o‘rniga ModelAdmin
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name',)
        }),
    )
  
   
    
    
# Rektorat Hodimlari
@admin.register(RectoratUserModel)
class RectoratUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'qabul_day_uz', 'number', 'email')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email')
    list_per_page = 20
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'qabul_day_uz', 'qabul_day_en', 'qabul_day_ru')
        }),
        ('Qo‘shimcha ma\'lumotlar', {
            'fields': ('body_uz', 'body_en', 'body_ru')
        }),
    )

@admin.register(UserModel)
class UserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'number', 'email', 'tg_uz')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email', 'tg_uz', 'tg_en', 'tg_ru')
    list_per_page = 20
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'tg_uz', 'tg_en', 'tg_ru')
        }),
    )

# Fakultetlar
@admin.register(FacultetUserModel)
class FacultetUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'qabul_day_uz', 'number', 'email')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email')
    list_per_page = 20
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'qabul_day_uz', 'qabul_day_en', 'qabul_day_ru')
        }),
        ('Qo‘shimcha ma\'lumotlar', {
            'fields': ('body_uz', 'body_en', 'body_ru')
        }),
    )

@admin.register(FacultetInUserModel)
class FacultetInUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'number', 'email', 'tg_uz')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email', 'tg_uz', 'tg_en', 'tg_ru')
    list_per_page = 20
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'tg_uz', 'tg_en', 'tg_ru')
        }),
    )

# Markazlar
@admin.register(MarkazUserModel)
class MarkazUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'qabul_day_uz', 'number', 'email')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email')
    list_per_page = 20
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'qabul_day_uz', 'qabul_day_en', 'qabul_day_ru')
        }),
        ('Qo‘shimcha ma\'lumotlar', {
            'fields': ('body_uz', 'body_en', 'body_ru')
        }),
    )

@admin.register(MarkazInUserModel)
class MarkazInUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'number', 'email', 'tg_uz')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email', 'tg_uz', 'tg_en', 'tg_ru')
    list_per_page = 20
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'tg_uz', 'tg_en', 'tg_ru')
        }),
    )

# Bo‘limlar
@admin.register(BulimUserModel)
class BulimUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'qabul_day_uz', 'number', 'email')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email')
    list_per_page = 20
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'qabul_day_uz', 'qabul_day_en', 'qabul_day_ru')
        }),
        ('Qo‘shimcha ma\'lumotlar', {
            'fields': ('body_uz', 'body_en', 'body_ru')
        }),
    )

@admin.register(BulimInUserModel)
class BulimInUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'number', 'email', 'tg_uz')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email', 'tg_uz', 'tg_en', 'tg_ru')
    list_per_page = 20
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'tg_uz', 'tg_en', 'tg_ru')
        }),
    )

# Kafedralar
@admin.register(KafedraUserModel)
class KafedraUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'qabul_day_uz', 'number', 'email')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email')
    list_per_page = 20
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'qabul_day_uz', 'qabul_day_en', 'qabul_day_ru')
        }),
        ('Qo‘shimcha ma\'lumotlar', {
            'fields': ('body_uz', 'body_en', 'body_ru')
        }),
    )

@admin.register(KafedraInUserModel)
class KafedraInUserModelAdmin(TranslationAdmin):
    list_display = ('name_uz', 'rang_uz', 'category', 'number', 'email', 'tg_uz')
    list_filter = ('category',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'email', 'tg_uz', 'tg_en', 'tg_ru')
    list_per_page = 20
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': ('name_uz', 'name_en', 'name_ru', 'rang_uz', 'rang_en', 'rang_ru', 'category', 'photo')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email', 'tg_uz', 'tg_en', 'tg_ru')
        }),
    )




@admin.register(HistoryUniversity)
class HistoryUniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields':(
                ('name_uz', 'name_en', 'name_ru'),
                ('body_uz', 'body_en', 'body_ru'),
                ('body', 'photo'),
            ) 
        }),
    )
    

@admin.register(AboutUsUniversity)
class AboutUsUniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields':(
                ('name_uz', 'name_en', 'name_ru'),
                ('body_uz', 'body_en', 'body_ru'),
                ('body', 'photo'),
            ) 
        }),
    )
    


@admin.register(CallUserModel)
class CallUserModelAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'number', 'email')
    fieldsets = (
        ('Umumiy ma\'lumotlar', {
            'fields': (
                ('name_uz', 'name_en', 'name_ru'),
                ('body_uz', 'body_en', 'body_ru'),
                ('rang_uz', 'rang_en', 'rang_ru'),
                ('qabul_day_uz', 'qabul_day_en', 'qabul_day_ru'),
                'photo'
            )
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('number', 'email')
        }),
    )