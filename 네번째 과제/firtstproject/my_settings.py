import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'django-insecure-_nfw*t=y)x!rhuu=63iuq*opos!4)$lzvv1c2ecuej%az(z8p7'