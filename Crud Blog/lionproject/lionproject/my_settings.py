import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'django-insecure-(-+v%+q&=93om62zz_r-odkke@zyhw^b$97%7gwupx(*%#o1l6'