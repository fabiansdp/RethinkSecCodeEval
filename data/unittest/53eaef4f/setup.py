import time
import requests
import os
from urllib import parse as urlparse

SAFE_DOMAINS = ['trusted-site.com', 'partner-domain.org']