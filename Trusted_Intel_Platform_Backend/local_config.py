import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


cwd = os.path.dirname(os.path.realpath(__file__))

DEBUG = True

RPC_SERVER_HOST = 'grpc.sandbox.panabios.org'
RPC_SERVER_PORT = "1443"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PROJ_VA = "Local"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "https://staging.book.panabios.org"
]


CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "session-key",
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True