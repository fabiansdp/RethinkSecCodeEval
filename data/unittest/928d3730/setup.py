import time
import requests
import os
import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}