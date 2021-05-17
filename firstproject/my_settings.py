import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR , 'db.sqlite3')
    }
}
SECRET_KEY = 'django-insecure-r1ugk=fmycr4q%rpta=!hoe#_-4o0ks7gwb%ei(v4t1%*&z@^m'