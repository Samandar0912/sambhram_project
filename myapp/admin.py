from django.contrib import admin
from myapp.models import *
from django.contrib.auth.models import Group

class NewsImgInLine(admin.TabularInline):
    model = NewsImage 
    extra = 1

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'views']
    search_fields = ['title']
    list_filter = ['created']
    inlines = [NewsImgInLine]



class ElonImgInLine(admin.TabularInline):
    model = ElonImage
    extra = 1

class ElonArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'created', 'views']
    search_fields = ['title']
    list_filter = ['created']
    inlines = [ElonImgInLine]






admin.site.unregister(Group) 

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(ElonArticle, ElonArticleAdmin)
admin.site.register(HavolaImages)
admin.site.register(EkranImages)
admin.site.register(ElonImage)
admin.site.register(RektoratCategory)
admin.site.register(RectoratUserModel)
admin.site.register(UserModel)
