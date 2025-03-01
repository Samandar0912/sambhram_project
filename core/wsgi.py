import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# BASE_DIR ni aniqlash
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django sozlamalarini o'rnatish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# WSGI ilovasini olish
application = get_wsgi_application()

# WhiteNoise bilan static fayllarni xizmat qilish uchun konfiguratsiya
application = WhiteNoise(application)

# Static fayllar papkasini qo'shish
application.add_files(os.path.join(BASE_DIR, 'static'), prefix='static/')

# Qo'shimcha static fayllarni qo'shish (agar kerak bo'lsa)
application.add_files("/path/to/more/static/files", prefix="more-files/")