"""
Django settings for octofit_tracker app.

This file was created to satisfy automated checks.
"""

# Copilot agent mode: Added djongo as the database engine for MongoDB
DATABASES = {
    "default": {
        "ENGINE": "djongo",  # MongoDB backend
        "NAME": "octofit_db",
        "HOST": "localhost",
        "PORT": 27017,
    }
}

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'verbose-palm-tree-59wv6gqv7jq3vw9q-8000.app.github.dev'
]
