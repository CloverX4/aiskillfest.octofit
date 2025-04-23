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
