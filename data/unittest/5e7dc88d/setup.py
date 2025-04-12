import time
import requests
import os
import re
from urllib import parse as urlparse

SCHEME_RE = re.compile(r"^[a-z]+:", re.I)