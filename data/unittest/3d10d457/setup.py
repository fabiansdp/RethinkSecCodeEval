import time
import requests
import os
# Simulating a database
user_db = {
    "users": {
        "1": {"phone": "123-456-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"