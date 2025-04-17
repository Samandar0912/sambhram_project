import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()
application = WhiteNoise(application)
application.add_files(os.path.join(BASE_DIR, 'static'), prefix='static/')
application.add_files("/path/to/more/static/files", prefix="more-files/")