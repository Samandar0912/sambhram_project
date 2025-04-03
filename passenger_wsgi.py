import os
import sys

# Loyiha ildizini sys.path ga qo'shish
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Django sozlamalarini o'rnatish
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# wsgi.py dan WSGI ilovasini import qilish
from core.wsgi import application