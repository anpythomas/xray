from decouple import config

from .base import *

print("prod")
SECRET_KEY = config("SECRET_KEY")
# HOSTED_ZONE_1 = config("HOSTED_ZONE_1")

DEBUG = False
ALLOWED_HOSTS = [
    config("HOSTED_ZONE_1")    
]

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True