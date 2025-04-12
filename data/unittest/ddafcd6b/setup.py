import time
import requests
import os
MAX_REQUESTS_PER_CLIENT = 100  # Max 100 requests per client
TIME_WINDOW = 3600  # 1-hour time window in seconds