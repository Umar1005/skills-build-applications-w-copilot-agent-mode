# Add 'tracker' to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'tracker',
    'octofit_tracker',  # Added octofit_tracker to INSTALLED_APPS
    'corsheaders',
]

# Add MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Enable CORS
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['*']

# Allow all hosts
ALLOWED_HOSTS = ['*']