import time
import requests
import os
# Simulating a database
user_database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
VALID_CSRF_TOKEN = "secure_csrf_token"