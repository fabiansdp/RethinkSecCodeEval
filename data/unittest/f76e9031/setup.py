import time
import requests
import os
from urllib.parse import urlparse
SAFE_REDIRECT_DOMAINS = ["trusted-redirect.com", "partner.com"]