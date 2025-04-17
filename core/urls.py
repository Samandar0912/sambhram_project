from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.i18n import set_language
from django.conf import settings
from django.conf.urls.static import static

# Asosiy URL sozlamalari
base_urlpatterns = [
    path('set-language/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
]

# i18n (tilga bog'liq) URL sozlamalari
i18n_urlpatterns = i18n_patterns(
    path('', include('myapp.urls')),
)

# Statik va media fayllar uchun URL sozlamalari
static_urlpatterns = (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

# Yakuniy URL ro'yxati
urlpatterns = base_urlpatterns + i18n_urlpatterns + static_urlpatterns