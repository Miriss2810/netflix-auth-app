from pathlib import Path

# BASE_DIR apunta a la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# CLAVE SECRETA (no la compartas en producción)
SECRET_KEY = 'django-insecure-...'

# SOLO para desarrollo
DEBUG = True

ALLOWED_HOSTS = []

# ------------------- INSTALLED_APPS -------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps externas
    'rest_framework',
    'corsheaders',         # 👈 CORS HEADERS

    # Tus apps
    'users',
]

# ------------------- MIDDLEWARE -------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 👈 DEBE IR PRIMERO
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------- URLS / WSGI -------------------
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# ------------------- DATABASE -------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------- PASSWORD VALIDATION -------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ------------------- INTERNATIONALIZATION -------------------
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# ------------------- STATIC FILES -------------------
STATIC_URL = '/static/'

# ------------------- DEFAULT PRIMARY KEY -------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------- CUSTOM USER -------------------
AUTH_USER_MODEL = 'users.CustomUser'

# ------------------- CORS -------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # 👈 React app (frontend)
]
